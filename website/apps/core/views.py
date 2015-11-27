from django.db.models import Count
from django.conf import settings
from django.http import Http404, HttpResponse
from django.template import RequestContext, loader
from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.views.generic import DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator
from itertools import chain
from website.apps.core.models import Source, Culture, Language, Section, Category, Glossary, Publication
from website.apps.core.forms import CultureForm, SourceForm, RegistrationForm, ContactForm, PublicationForm
from website.apps.survey.models import Question, Response
import json
from axes.utils import reset
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from collections import defaultdict, OrderedDict
from django.contrib.auth.forms import *
from django.contrib.auth.views import password_reset, password_reset_complete
from django_tables2 import SingleTableView
from django.core.mail import send_mail, BadHeaderError
from django.core.cache import cache

class DefaultListOrderedDict(OrderedDict):
    def __missing__(self,k):
        self[k] = []
        return self[k]


class RobotsTxt(TemplateView):
	"""Simple robots.txt implementation"""
	template_name = "robots.txt"
	content_type = "text/plain"


def logUserIn(request):
    if request.method == 'POST':
        login(request, template_name='login.html')
    elif request.method == 'GET':
        return render_to_response('login.html', {'form':AuthenticationForm()}, context_instance=RequestContext(request))


def resetPW(request):
    return password_reset(request)

def PWreset(request):
    client_ip = request.META['REMOTE_ADDR']
    reset(ip=client_ip)
    reset(username = request.user.username)
    return password_reset_complete(request)


def frontPage(request):
	cultures = Culture.objects.all().values_list('culture', 'slug')
        return render_to_response('index.html', {'cultures':cultures.count()}, context_instance=RequestContext(request))

	
def glossary(request):
    terms = Glossary.objects.all()
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', \
'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X','Y', 'Z']
    glossaryDict = DefaultListOrderedDict()
    for a in alphabets:
        glossaryDict[a].append(None)

    for t in terms:
        firstLetter = str(t.term)[0]
        glossaryDict[firstLetter].append(t)

    return render_to_response('glossary.html', {'terms':OrderedDict(glossaryDict)}, context_instance=RequestContext(request))
	
def CultureIndex(request):
	"""Culture Index"""
	template = loader.get_template('core/culture_index.html')

	locations = []
	cultures = []
	for c in Culture.objects.all():
		cultureResponses = Response.objects.all().filter(culture=c)
		if c.ethonyms is not None:
			ethonyms = c.ethonyms.split('; ')
			for e in ethonyms:
				if len(e) > 0:
					cultures.append({
					'culture':e,
					'slug':c.slug
					})
		cultures.append({
			'culture':c.culture,
			'slug':c.slug
		})
		cultures.sort()
		ethonymDict = DefaultListOrderedDict()
                alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

                for a in alphabets:
                    ethonymDict[a].append(None)

                for d in cultures:
                    firstLetter = d['culture'][0]
                    ethonymDict[firstLetter].append(d)


                try:
			lat = cultureResponses.filter(question__simplified_question='Latitude')[0].response
			longi = cultureResponses.filter(question__simplified_question='Longitude')[0].response
		except:
			lat = None
			longi = None
		if lat is not None and longi is not None:
			locations.append({"lat": lat, "long":longi, "culture": c.culture, "slug":c.slug})
	
	return render_to_response('core/culture_index.html', {'ethonyms':OrderedDict(ethonymDict),'latlong':locations}, context_instance=RequestContext(request),)

	
def compareCultures(request):
	"""Culture Index"""
	template = loader.get_template('core/compare_cultures.html')

	if request.is_ajax():
		
			toRetrieve = request.GET.get('question')
			data = []
			try:
				quest = Question.objects.all().filter(question__exact=toRetrieve)[0]
			except:
				quest = Question.objects.all().filter(simplified_question=toRetrieve)[0]
			choices = quest.get_choices()
			startsAtZero = False
			for a in choices:
				if any ("0" in s for s in a):
					startsAtZero = True
					break

			choices = quest.get_pub_choices()
			for r in Response.objects.all().filter(question=quest).exclude(missing=True):
				try:
					latitude = Response.objects.all().filter(culture=r.culture).filter(question__simplified_question='Latitude')[0].response
					longitude = Response.objects.all().filter(culture=r.culture).filter(question__simplified_question='Longitude')[0].response
				#if latitude is not None and longitude is not None:
				except:
					latitude = None
					longitude = None
				data.append({"Zero":startsAtZero, "choices":choices, "response":str(r.response), "culture":str(r.culture), "slug": r.culture.slug, "latitude":latitude, "longitude":longitude})
			return HttpResponse(json.dumps(data), content_type='application/json')
	
	locations = []
	
	for c in Culture.objects.all():
		cultureResponses = Response.objects.all().filter(culture=c)
		try:
			lat = cultureResponses.filter(question__simplified_question='Latitude')[0].response
			longi = cultureResponses.filter(question__simplified_question='Longitude')[0].response
		except:
			lat = None
			longi = None
		if lat is not None and longi is not None:
			locations.append({"lat": lat, "long":longi, "culture": c.culture, "slug":c.slug})
	
	
	categories = Category.objects.all().order_by('number')
	questions = Question.objects.all().filter(response_type=Question.RESPONSETYPE_OPTION).order_by('section__number')
	fullDict = defaultdict(list)
	
	for c in categories:
		subsections = Section.objects.all().filter(category=c).order_by('number').exclude(section__contains='Time Focus')
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
			
	return render_to_response('core/compare_cultures.html', {
	'latlong':locations, 'full':dict(fullDict)}, context_instance=RequestContext(request),)

	
def details(request, slug):

	culture = get_object_or_404(Culture, slug=slug)
	#get all responses for this culture
	cacheName = 'full'+culture.culture
        if cache.get(cacheName) is not None:
            return cache.get(cacheName)

        queryset = Response.objects.all().filter(culture=culture)
	#queryset = queryset.exclude(question__displayPublic=True)

	#get languages
	langs = culture.languages.all()
	#get latitude and longitude (for map of location)
	postCtime = ''
	categories = Category.objects.all().order_by('number')
	send = []
	
	try:
		latitude = queryset.filter(question__simplified_question='Latitude')[0].response
		longitude = queryset.filter(question__simplified_question='Longitude')[0].response
	except:
		latitude = None
		longitude = None
	
	timeF =  queryset.filter(question__section__section__contains='Time Focus').order_by('question__section__number')
	
        source_list = set() #get list of sources for references section
	for r in queryset:
		if r.source1 is not None and str(r.source1) != 'Source not applicable (2014)':
			source_list.add(r.source1)
		if r.source2 is not None:
			source_list.add(r.source2)
		if r.source3 is not None:
			source_list.add(r.source3)
		if r.source4 is not None:
			source_list.add(r.source4)
		if r.source5 is not None:
			source_list.add(r.source5)
	source_list = sorted(source_list, key=lambda source:source.reference, reverse=False)

	fullDict = defaultdict(list)
	
	for c in categories:
            
	
		subsections = Section.objects.all().filter(category=c).order_by('number').exclude(section__contains='Time Focus')
		subsectionDict = DefaultListOrderedDict()
		for section in subsections:
			filt = queryset.filter(question__subsection=section).order_by('question__section__number', 'question__publicNumber')
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
                    added = False
                
                    for t in timeF:
                        if c.number is t.question.subsection.number and not c.timeFocus:
                            send.append({
                                    'category':c,
                                    'time':t.response
                                    })
                            added = True
                            break;
                        else:
                            continue;
                        
                    if not added and not c.timeFocus:
                            num = c.number
                            try:
                                before = timeF.filter(question__section__number=(num-1))[0].response
                                after = timeF.filter(question__section__number=(num+1))[0].response
                                if before.find('-') is not -1 and after.find('-') is not -1:
                                    send.append({
                                            'category':c,
                                            'time':before.partition('-')[2]+'-'+after.partition('-')[0]
                                    })
                                elif before.find('-') is not -1:
                                    send.append({
                                            'category':c,
                                            'time':before.partition('-')[2]+'-'+after
                                    })
                                elif after.find('-') is not -1:
                                    send.append({
                                            'category':c,
                                            'time':before+'-'+after.partition('-')[0]
                                    })
                                else:
                                    send.append({
                                            'category':c,
                                            'time':before+'-'+after
                                    })
                            except:
                                send.append({
                                        'category':c,
                                        'time':'?'
                                })
                    elif not added and c.timeFocus:
                            send.append({
                                    'category':c
                            })

        cache.set(cacheName, render_to_response('core/culture_detail.html', {'culture': culture, 'langs': langs, 'longitude':longitude, 'latitude':latitude, 'time':send, 'source_list':source_list, 'full':dict(fullDict)}, context_instance=RequestContext(request)), 9600)
        
	return render_to_response('core/culture_detail.html', 
		{'culture': culture, 'langs': langs, 'longitude':longitude, 'latitude':latitude, 'time':send, 'source_list':source_list,
		'full':dict(fullDict)},
		
			context_instance=RequestContext(request))
	   
def getPublications(request):
	questions = Question.objects.all().filter(displayPublic=False)
	cultures = Culture.objects.all().count()
	religiousBelief = questions.filter(subsection__section__contains='Belief').count()
	practice = questions.filter(subsection__section__contains='Practice').count()
	socialEnv = questions.filter(subsection__section__contains='Social Environment').count()
	physEnv = questions.filter(subsection__section='Physical Environment').count()
        physEnv += questions.filter(subsection__section__contains='Physical Environment').count()
	return render_to_response('about.html', {'cultures':cultures, 'relBelief':religiousBelief, 'relPractice':practice,
		'publications':Publication.objects.all().order_by('reference'), 'social':socialEnv, 'physical':physEnv,
		'questions':questions.count()}, context_instance=RequestContext(request))

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
	return render_to_response('admin/AddPublication.html', {'form': form}, context_instance=RequestContext(request))

def contact_form(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			comment = form.cleaned_data['comment']
			message = 'Name: ' + name + '\n\nEmail: ' + email+ '\n\nComments: ' + comment		
			try:
				send_mail("Contact Us Pulotu", message, "pulotu@josephwatts.org", ['pulotu@josephwatts.org',])			
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect(reverse('thankyou2'))
	else:
		form = ContactForm()

	return render(request, "contact.html", { "form" : form })

def request_form(request):
    from website.apps.survey.views import download_dataset
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            affiliation = form.cleaned_data['affiliation']
            email = form.cleaned_data['email']
            reason = form.cleaned_data['reason']
            message = 'Name: ' + name + '\n\nEmail: ' + email +'\n\nAffiliation: ' + affiliation + '\n\nReason for requesting dataset: ' + reason
            try:
                send_mail("A user has downloaded the Pulotu dataset", message, "pulotu@josephwatts.org", ['pulotu@josephwatts.org',])			
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            if cache.get('public') is not None:
                return cache.get('public')
            response = download_dataset(request)
            return response
            #return redirect('conditionsofuse')
    else:
        form = RegistrationForm()
    return render(request, "dataset.html", { "form" : form })

@login_required()
def CultureEdit(request, slug=None):
	"Editing of Cultures"
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
	
	return render_to_response('core/culture_edit.html', {
		'form': form, 'culture': c
	}, context_instance=RequestContext(request))

	

@login_required()
def SourceEdit(request, slug=None):
	
	"Editing of Sources"
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
	
	return render_to_response('core/source_edit.html', {
		'form': form, 'source': s
	}, context_instance=RequestContext(request))
