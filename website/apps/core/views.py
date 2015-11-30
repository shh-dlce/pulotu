from collections import defaultdict, OrderedDict
from string import ascii_uppercase

from django.http import HttpResponse
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from website.apps.core.models import (
    Source, Culture, Section, Category, Glossary, Publication,
)
from website.apps.core.forms import CultureForm, SourceForm, ContactForm, PublicationForm
from website.apps.survey.models import Question, Response
import json
from axes.utils import reset
from django.contrib.auth.forms import *
from django.contrib.auth.views import password_reset, password_reset_complete
from django.core.mail import send_mail, BadHeaderError
from django.core.cache import cache

#
# FIXME: can we send email with this from address?
#
MAIL_FROM = "pulotu@josephwatts.org"
MAIL_TO = [MAIL_FROM]


class DefaultListOrderedDict(OrderedDict):
    def __missing__(self, k):
        self[k] = []
        return self[k]


def sources(responses):
    refs = set()
    for r in responses:
        if r.source1 is not None \
                and str(r.source1) != 'Source not applicable (2014)':
            refs.add(r.source1)
        if r.source2 is not None:
            refs.add(r.source2)
        if r.source3 is not None:
            refs.add(r.source3)
        if r.source4 is not None:
            refs.add(r.source4)
        if r.source5 is not None:
            refs.add(r.source5)
    return sorted(refs, key=lambda source: source.reference, reverse=False)


def latlon(cultures):
    res = {}
    for query in 'Latitude', 'Longitude':
        qs = cultures.filter(question__simplified_question=query)
        if qs:
            res[query] = qs[0].response
    return res.get('Latitude'), res.get('Longitude')


def mail(subject, message):
    try:
        send_mail(subject, message, MAIL_FROM, MAIL_TO)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')


class RobotsTxt(TemplateView):
    """Simple robots.txt implementation"""
    template_name = "robots.txt"
    content_type = "text/plain"


def logUserIn(request):
    if request.method == 'POST':
        pass
        #
        # FIXME: It's impossible that the line below ever worked, because `login` wasn't
        # imported!
        #
        # login(request, template_name='login.html')
    elif request.method == 'GET':
        return render_to_response(
            'login.html',
            {'form': AuthenticationForm()},
            context_instance=RequestContext(request))


def resetPW(request):
    return password_reset(request)


def PWreset(request):
    reset(ip=request.META['REMOTE_ADDR'])
    reset(username=request.user.username)
    return password_reset_complete(request)


def frontPage(request):
    return render_to_response(
        'index.html',
        {'cultures': Culture.objects.all().values_list('culture', 'slug').count()},
        context_instance=RequestContext(request))


def glossary(request):
    glossaryDict = DefaultListOrderedDict()
    for a in ascii_uppercase:
        glossaryDict[a].append(None)

    for t in Glossary.objects.all():
        glossaryDict[str(t.term)[0]].append(t)

    return render_to_response(
        'glossary.html',
        {'terms': OrderedDict(glossaryDict)},
        context_instance=RequestContext(request))


def CultureIndex(request):
    """Culture Index"""
    locations = []
    cultures = []
    for c in Culture.objects.all():
        if c.ethonyms:
            for e in c.ethonyms.split('; '):
                if len(e) > 0:
                    cultures.append({'culture': e, 'slug': c.slug})
        cultures.append({'culture': c.culture, 'slug': c.slug})
        cultures.sort()

        lat, longi = latlon(Response.objects.all().filter(culture=c))
        if lat is not None and longi is not None:
            locations.append(
                {"lat": lat, "long": longi, "culture": c.culture, "slug": c.slug})

    ethonymDict = DefaultListOrderedDict()
    for a in ascii_uppercase:
        ethonymDict[a].append(None)
    for d in cultures:
        ethonymDict[d['culture'][0]].append(d)

    return render_to_response(
        'core/culture_index.html',
        {'ethonyms': OrderedDict(ethonymDict), 'latlong': locations},
        context_instance=RequestContext(request), )


def compareCultures(request):
    """Culture Index"""
    if request.is_ajax():
        toRetrieve = request.GET.get('question')
        data = []
        quest = Question.objects.all().filter(question__exact=toRetrieve)
        if not quest:
            quest = Question.objects.all().filter(simplified_question=toRetrieve)
        assert quest
        quest = quest[0]
        startsAtZero = False
        for a in quest.get_choices():
            if any("0" in s for s in a):
                startsAtZero = True
                break

        for r in Response.objects.all().filter(question=quest).exclude(missing=True):
            latitude, longitude = latlon(Response.objects.all().filter(culture=r.culture))
            data.append({
                "Zero": startsAtZero,
                "choices": quest.get_pub_choices(),
                "response": str(r.response),
                "culture": str(r.culture),
                "slug": r.culture.slug,
                "latitude": latitude,
                "longitude": longitude})
        return HttpResponse(json.dumps(data), content_type='application/json')

    locations = []

    for c in Culture.objects.all():
        cultureResponses = Response.objects.all().filter(culture=c)
        lat, longi = latlon(cultureResponses)
        if lat is not None and longi is not None:
            locations.append(
                {"lat": lat, "long": longi, "culture": c.culture, "slug": c.slug})

    categories = Category.objects.all().order_by('number')
    questions = Question.objects.all() \
        .filter(response_type=Question.RESPONSETYPE_OPTION).order_by('section__number')
    fullDict = defaultdict(list)

    for c in categories:
        subsections = Section.objects.all() \
            .filter(category=c).order_by('number').exclude(section__contains='Time Focus')
        subsectionDict = DefaultListOrderedDict()
        for section in subsections:
            filt = questions.filter(subsection=section)
            nary = DefaultListOrderedDict()
            for q in filt:
                if not q.displayPublic and not request.user.is_authenticated():
                    nary[str(q.section)].append(q)
                elif request.user.is_authenticated():
                    nary[str(q.section)].append(q)

            if nary:
                subsectionDict[str(section)].append(OrderedDict(nary))
        fullDict[str(c)].append(OrderedDict(subsectionDict))

    return render_to_response(
        'core/compare_cultures.html',
        {'latlong': locations, 'full': dict(fullDict)},
        context_instance=RequestContext(request))


def details(request, slug):
    culture = get_object_or_404(Culture, slug=slug)
    # get all responses for this culture
    cacheName = 'full' + culture.culture
    if cache.get(cacheName) is not None:
        return cache.get(cacheName)

    queryset = Response.objects.all().filter(culture=culture)

    categories = Category.objects.all().order_by('number')
    send = []

    timeF = queryset \
        .filter(question__section__section__contains='Time Focus') \
        .order_by('question__section__number')
    latitude, longitude = latlon(queryset)

    fullDict = defaultdict(list)

    for c in categories:
        subsections = Section.objects.all() \
            .filter(category=c).order_by('number').exclude(section__contains='Time Focus')
        subsectionDict = DefaultListOrderedDict()
        for section in subsections:
            filt = queryset \
                .filter(question__subsection=section) \
                .order_by('question__section__number', 'question__publicNumber')
            nary = DefaultListOrderedDict()
            for q in filt:
                if not q.question.displayPublic and not q.missing:
                    nary[str(q.question.section)].append(q)
            try:
                if nary:
                    subsectionDict[str(section)].append(OrderedDict(nary))
            except:
                subsectionDict[str(section)].append('')

        if subsectionDict:
            fullDict[str(c)].append(OrderedDict(subsectionDict))

            d = {'category': c}

            for t in timeF:
                if c.number is t.question.subsection.number and not c.timeFocus:
                    d['time'] = t.response
                    break
            else:  # no time set
                if not c.timeFocus:
                    try:
                        before = timeF.filter(
                            question__section__number=(c.number - 1))[0].response
                        after = timeF.filter(
                            question__section__number=(c.number + 1))[0].response
                        if before.find('-') is not -1 and after.find('-') is not -1:
                            d['time'] = '-'.join(
                                [before.partition('-')[2], after.partition('-')[0]])
                        elif before.find('-') is not -1:
                            d['time'] = before.partition('-')[2] + '-' + after
                        elif after.find('-') is not -1:
                            d['time'] = before + '-' + after.partition('-')[0]
                        else:
                            d['time'] = before + '-' + after
                    except:
                        d['time'] = '?'
            send.append(d)

    res = render_to_response(
        'core/culture_detail.html',
        {
            'culture': culture,
            'langs': culture.languages.all(),
            'longitude': longitude,
            'latitude': latitude,
            'time': send,
            'source_list': sources(queryset),
            'full': dict(fullDict)
        },
        context_instance=RequestContext(request))
    cache.set(cacheName, res, 9600)
    return res


def getPublications(request):
    questions = Question.objects.all().filter(displayPublic=False)
    ctx = dict(
        questions=questions.count(),
        publications=Publication.objects.all().order_by('reference'),
        cultures=Culture.objects.all().count())
    for k, term in [
        ('relBelief', 'Belief'),
        ('relPractice', 'Practice'),
        ('social', 'Social Environment'),
        ('physical', 'Physical Environment'),
    ]:
        ctx[k] = questions.filter(subsection__section__contains=term).count()

    return render_to_response('about.html', ctx, context_instance=RequestContext(request))


@login_required()
def AddPublication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            s = form.save(commit=False)
            s.editor = request.user
            s.save()
            return redirect(reverse('about'))

    else:
        form = PublicationForm()
    return render_to_response(
        'admin/AddPublication.html',
        {'form': form},
        context_instance=RequestContext(request))


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']
            message = 'Name: ' + name + '\n\nEmail: ' + email + '\n\nComments: ' + comment
            mail("Contact Us Pulotu", message)
            return redirect(reverse('thankyou2'))
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})


@login_required()
def CultureEdit(request, slug=None):
    """Editing of Cultures"""
    if slug is None:
        c = None
        form = CultureForm(request.POST or None)
    else:
        c = get_object_or_404(Culture.objects, slug=slug)
        form = CultureForm(request.POST or None, instance=c)

    if form.is_valid():
        c = form.save(commit=False)
        if not c.slug:
            c.slug = slugify(c.culture)
        c.editor = request.user
        c.save()
        form.save_m2m()
        return redirect(reverse('survey-culture-index', kwargs={"slug": c.slug}))

    return render_to_response(
        'core/culture_edit.html',
        {'form': form, 'culture': c},
        context_instance=RequestContext(request))


@login_required()
def SourceEdit(request, slug=None):
    """Editing of Sources"""
    if slug is None:
        s = None
        form = SourceForm(request.POST or None)
    else:
        s = get_object_or_404(Source, slug=slug)
        form = SourceForm(request.POST or None, instance=s)

    if form.is_valid():
        s = form.save(commit=False)
        if not s.slug:
            s.slug = slugify("".join([str(s.author), str(s.year)]))
        s.editor = request.user
        s.save()
        return redirect(reverse('admin:core_source_changelist'))

    return render_to_response(
        'core/source_edit.html',
        {'form': form, 'source': s},
        context_instance=RequestContext(request))
