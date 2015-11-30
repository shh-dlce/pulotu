# -*- coding: utf-8 -*-
from django.db.models import Count
from django.http import Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import DetailView, TemplateView
from django.core.urlresolvers import reverse
from website.apps.core.models import Section, Culture, Category
from website.apps.survey.models import Question, Response
from website.apps.survey.forms import construct_section_forms
from website.apps.survey.tables import SurveyIndexTable, SurveyCultureIndexTable
from django.http import HttpResponse, HttpResponseRedirect
import csv
from collections import defaultdict, OrderedDict
from website.apps.core.views import DefaultListOrderedDict, sources
from django.core.cache import cache


def _download(filename):
    response = HttpResponse(content_type='text')
    response['Content-Disposition'] = 'attachment; filename=' + filename
    return response


class SurveyIndex(TemplateView):
    """Survey Index"""
    model = Culture
    template_name = 'survey/survey_index.html'

    def get_context_data(self, **kwargs):
        context = super(SurveyIndex, self).get_context_data(**kwargs)

        # get counts
        totalq = Question.objects.count()
        answered = {}
        for d in Culture.objects.values('id').annotate(Count('response')):
            answered[d['id']] = d['response__count']

        object_list = []
        for obj in Culture.objects.all():
            obj.qdone = answered.get(obj.id, 0)
            obj.qtodo = totalq - answered.get(obj.id, 0)
            missing = 0
            for r in Response.objects.filter(culture=obj):
                if r.missing:
                    missing += 1
            obj.qmissing = missing
            object_list.append(obj)

        context['table'] = SurveyIndexTable(object_list)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SurveyIndex, self).dispatch(*args, **kwargs)


@login_required()
def indexx(request, slug):
    sections = []
    fullDict = defaultdict(list)
    culture = Culture.objects.all().filter(slug=slug)
    if culture:
        culture = culture[0]
    else:
        raise Http404('culture does not exist')
    # get saved responses..
    responses = {}
    question = {}
    missing = {}
    resp = Response.objects.filter(culture=culture).select_related('question')
    questions = Question.objects.all().order_by('number')
    for r in resp:
        sect_id = r.question.section_id
        responses[sect_id] = responses.get(sect_id, 0) + 1
        if r.missing:
            missing[sect_id] = missing.get(sect_id, 0) + 1
    for s in Section.objects.all().annotate(questions=Count('question')):
        s.culture = culture
        s.answered = responses.get(s.id, 0)
        s.qmissing = missing.get(s.id, 0)
        question[s.id] = s.questions
        if s.questions is not 0:
            s.questions = s.questions - s.answered
            sections.append(s)

    for c in Category.objects.all().order_by('number'):
        subsections = Section.objects.all().filter(category=c).order_by('number')
        subDict = DefaultListOrderedDict()
        for s in subsections:
            for q in questions.filter(subsection=s):
                if q.section not in subDict[str(q.subsection)]:
                    q.section.answered = responses.get(q.section.id, 0)
                    q.section.questions = question.get(q.section.id, 0) \
                        - q.section.answered
                    q.section.culture = culture.slug
                    q.section.missing = missing.get(q.section.id, 0)
                    subDict[str(q.subsection)].append(q.section)

        fullDict[str(c)].append(OrderedDict(subDict))

    return render_to_response(
        'survey/survey_culture_index1.html',
        {'culture': dict(fullDict), 'full': sections, 'object': culture},
        context_instance=RequestContext(request))


class SurveyCultureIndex(DetailView):
    """Survey Culture Sub-Index"""
    model = Culture
    template_name = 'survey/survey_culture_index.html'

    def get_context_data(self, **kwargs):
        context = super(SurveyCultureIndex, self).get_context_data(**kwargs)
        sections = []
        # get saved responses..
        responses = {}
        missing = {}
        resp = Response.objects.filter(
            culture=kwargs['object']).select_related('question')
        for r in resp:
            sect_id = r.question.section_id
            responses[sect_id] = responses.get(sect_id, 0) + 1
            if r.missing:
                missing[sect_id] = missing.get(sect_id, 0) + 1
        for s in Section.objects.all().annotate(questions=Count('question')):
            s.culture = kwargs['object']
            s.toanswer = responses.get(s.id, 0)
            s.qmissing = missing.get(s.id, 0)
            if s.questions is not 0:
                s.questions = s.questions - s.toanswer
                sections.append(s)
        context['table'] = SurveyCultureIndexTable(sections)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SurveyCultureIndex, self).dispatch(*args, **kwargs)


@login_required()
def SurveySectionEdit(request, culture, section):
    "Editing of Survey Section"
    culture_obj = get_object_or_404(Culture, slug=culture)
    section_obj = get_object_or_404(Section, slug=section)
    forms = construct_section_forms(post_data=request.POST or None,
                                    culture_obj=culture_obj,
                                    section_obj=section_obj)

    status = []
    # save if necessary
    if request.method == 'POST':
        all_valid = True
        for form in forms:
            if form.is_valid():
                obj = form.save(commit=False)
                obj.author = request.user
                obj.culture = culture_obj
                obj.save()
                status.append(
                    "Saved Response to question {0}.{1}".format(
                        section_obj.id, obj.question.number))
            else:
                all_valid = False
                # if all forms are valid. Return to survey culture index
        if all_valid:
            return HttpResponseRedirect(
                reverse('survey-culture-index', kwargs={"slug": culture}))
            # if not, fall through to the survey section edit again.
    return render_to_response('survey/survey_section_edit.html', {
        'forms': forms, 'culture': culture_obj, 'section': section_obj, 'status': status,
    }, context_instance=RequestContext(request))


def _stringify(s, encoding, errors):
    if s is None:
        return ''
    if isinstance(s, unicode):
        return s.encode(encoding, errors)

    if isinstance(s, (int, float)):
        pass  # let csv.QUOTE_NONNUMERIC do its thing.
    elif not isinstance(s, str):
        s = str(s)
    return s


def _stringify_list(l, encoding, errors='strict'):
    try:
        return [_stringify(s, encoding, errors) for s in iter(l)]
    except TypeError as e:
        raise csv.Error(str(e))


def _unicodify(s, encoding):
    if s is None:
        return None
    if isinstance(s, (unicode, int, float)):
        return s
    if isinstance(s, str):
        return s.decode(encoding)
    return s


class UnicodeWriter(object):
    def __init__(
            self, f, dialect=csv.excel, encoding='utf-8', errors='strict', *args, **kwds):
        self.encoding = encoding
        self.writer = csv.writer(f, dialect, *args, **kwds)
        self.encoding_errors = errors

    def writerow(self, row):
        self.writer.writerow(_stringify_list(row, self.encoding, self.encoding_errors))

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

    @property
    def dialect(self):
        return self.writer.dialect


def download_dataset(request):
    response = _download('pulotuDataset.txt')
    writer = UnicodeWriter(response, dialect=csv.excel_tab)
    cacheName = 'cache'
    headings = ['Culture']
    if request.user.is_authenticated():
        headings.append('Culture_Notes')
    headings.extend(['isocode', 'ABVD_Code'])

    def heading(q, label):
        return 'v' + str(q.number) + '.' + label.replace(' ', '_')

    if request.user.is_authenticated():
        questionlist = request.POST.getlist('questions')
        if not questionlist:
            return HttpResponse('<h1>Error, invalid POST data.</h1>', status=400)

        questions = Question.objects.all() \
            .filter(id__in=questionlist).order_by('number')
        if len(questions) == Question.objects.all().count():
            if cache.get('fulldataset') is not None:
                return cache.get('fulldataset')
            cacheName = 'fulldataset'
        for q in questions:
            if cacheName is not 'fulldataset':
                cacheName = cacheName + str(q.number)
            if q.simplified_question:
                headings.append(heading(q, q.simplified_question))
            else:
                headings.append(heading(q, q.question))
            for label in ['Source', 'Notes', 'Uncertainty']:
                headings.append(heading(q, label))
        if cache.get(cacheName) is not None:
            return cache.get(cacheName)
    else:
        # get all public questions
        questions = Question.objects.all().filter(displayPublic=False).order_by('number')
        for q in questions:
            if q.simplified_question:
                headings.append(heading(q, q.simplified_question))
            else:
                headings.append(heading(q, q.question))
            headings.append(heading(q, 'Source'))
    writer.writerow(headings)
    if cache.get('cultures') is None:
        cache.set('cultures', Culture.objects.all().prefetch_related('languages'))
    cultures = cache.get('cultures')
    responses = Response.objects.all()
    for culture in cultures:
        isocodes = []
        abvdcodes = []
        resplist = [culture.culture]
        # get language information
        for lang in culture.languages.all():
            if lang.abvdcode:
                if str(lang.abvdcode) not in abvdcodes:
                    abvdcodes.append(str(lang.abvdcode))
            if str(lang.isocode) not in isocodes:
                isocodes.append(str(lang.isocode))
        if request.user.is_authenticated():
            resplist.append(culture.notes)
        resplist.append('; '.join(isocodes))
        resplist.append('; '.join(abvdcodes) if abvdcodes else '')
        culture_responses = responses.filter(culture=culture).order_by('question__number')
        for q in questions:
            try:
                r = culture_responses.filter(question=q)[0]
            except:
                r = None
            if r is None:
                resplist.extend(['', ''])
                if request.user.is_authenticated():
                    resplist.extend(['', ''])
            else:
                if r.missing:
                    resplist.append('?')
                else:
                    try:
                        resplist.append(' '.join(r.response.split()))
                    except:
                        resplist.append(r.response)
                sources = '; '.join([
                    ' pp '.join(
                        map(str, [getattr(r, 'source' + i), getattr(r, 'page' + i)]))
                    for i in '12345' if getattr(r, 'source' + i)])

                resplist.append(' '.join(sources.split()))
                if request.user.is_authenticated():
                    resplist.extend([' '.join(r.codersnotes.split()), r.uncertainty])
        writer.writerow(resplist)
    cache.set(cacheName if request.user.is_authenticated() else 'public', response, 3600)
    return response


@login_required()
def chooseexport(request):
    if request.method == 'POST':
        return download_dataset(request)

    allquestions = Question.objects.all()
    for q in allquestions:
        if q.displayPublic is None:
            q.displayPublic = False

    fullDict = DefaultListOrderedDict()
    for c in Category.objects.all().order_by('number'):
        for section in Section.objects.all().filter(category=c).order_by('number'):
            fullDict[section].append(allquestions.filter(subsection=section))
    return render_to_response(
        'survey/excel_format.html',
        {'questions': OrderedDict(fullDict), 'exportinfo': ''},
        context_instance=RequestContext(request))


@login_required()
def download_references(request):
    if cache.get('refs') is not None:
        return cache.get('refs')

    response = _download('references.txt')
    writer = UnicodeWriter(
        response, delimiter='#', quoting=csv.QUOTE_NONE, escapechar=' ')
    allresponses = Response.objects.all().select_related('culture')
    for culture in Culture.objects.all():
        resps = allresponses.filter(culture=culture).select_related(
            'source1', 'source2', 'source3', 'source4', 'source5')
        writer.writerow([culture])
        for ref in sources(resps):
            writer.writerow([' '])
            writer.writerow([ref.reference])
        writer.writerow([' '])
        writer.writerow(['----------------------------------'])
    cache.set('refs', response, 3600)
    return response
