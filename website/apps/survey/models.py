import re
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from polymorphic import PolymorphicModel, ShowFieldType

from website.apps.core.models import TrackedModel, Category, Section, Culture, Source
from website.apps.statistics import statistic

OPTION_REGEX = re.compile(r"""^\s*?\((.*?)\)\s+(.*)$""", re.MULTILINE)
import watson

class Question(PolymorphicModel, TrackedModel):
	"""Stores Question Information"""

	RESPONSETYPE_INTEGER = 'Int'
	RESPONSETYPE_FLOAT = 'Float'
	RESPONSETYPE_TEXT = 'Text'
	RESPONSETYPE_OPTION = 'Option'
	
	RESPONSETYPE_CHOICES = (
		(RESPONSETYPE_INTEGER, 'Integer'),
		(RESPONSETYPE_FLOAT, 'Float'),
		(RESPONSETYPE_TEXT, 'Text'),
		(RESPONSETYPE_OPTION, 'Options')
	)
	
	subsection = models.ForeignKey(Section,  related_name="Section", verbose_name="Section",
		help_text="The broad section this question belongs to")
	section = models.ForeignKey(Section, verbose_name="Subsection",
		help_text="The specific section this question belongs to")
	publicNumber = models.IntegerField(blank=True, null=True, verbose_name="Public Number", help_text="For public order of questions")
	
	number = models.IntegerField(db_index=True,
		help_text="The sequence number for this question"
	) # should this be unique? 
	question = models.CharField(max_length=255, db_index=True, unique=True,
		help_text="The Question. Anything you do not want visible to the general public should go in the Information section."
	)

	simplified_question = models.CharField(max_length=255, 
		blank=True, null=True
	)
	information = models.TextField(blank=True,
		help_text="Information to display to the coder"
	)
	response_type = models.CharField(max_length=6, 
		choices=RESPONSETYPE_CHOICES,
		default=RESPONSETYPE_INTEGER,
		help_text="The expected response type"
	)
	
	#boolean variable to hide/show question from public
	displayPublic = models.BooleanField("Hide this question from the public", default=False)

	def __unicode__(self):
		return self.question

	@models.permalink
	def get_absolute_url(self):
		return ('question-detail', [self.id])

	class Meta:
		db_table = 'questions'


class OptionQuestion(Question):
	options = models.TextField(help_text="""The possible options. MUST be in the following format, with ONE option per line:
	 
	(?) Missing data
	(0) Low    
	(1) Moderate
	(2) High 
	""")

	
	def get_choices(self, with_empty=False):
		"""
		Returns a list of valid choices for this instance
		
		Parameter `with_empty` prepends an absence data code at the start of the list.
		"""
		choices = []
		for f in OPTION_REGEX.findall(self.options):
			choices.append((f[0].strip(), f[1].strip()))
		return choices
	
	def get_pub_choices(self, with_empty=False):
		choices = []
		for f in OPTION_REGEX.findall(self.options):
			choices.append(f[1].strip())
		return choices
		
		
	def get_choice(self, choice_id):
		"""Returns the text for a given choice_id"""
		for choice in self.get_choices():
			if choice[0] == choice_id:
				return choice[1]

	#def save(self, *args, **kwargs):
		# override save to set response_type to correct value.
	 #   self.response_type = Question.RESPONSETYPE_OPTION
	 #   super(OptionQuestion, self).save(*args, **kwargs)

	class Meta:
		db_table = 'questions_option'

class Response(ShowFieldType, PolymorphicModel):
	"""Stores information about a specific response"""
	added = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)
	question = models.ForeignKey(Question)
	culture = models.ForeignKey(Culture)
	#source = models.ForeignKey(Source)
	#source = models.ManyToManyField(Source, \
		#related_name='sources_info')
		
	source1 = models.ForeignKey(Source, blank=True, null=True, related_name="source1")
	source2 = models.ForeignKey(Source, blank=True, null=True, related_name="source2")
	source3 = models.ForeignKey(Source, blank=True, null=True, related_name="source3")
	source4 = models.ForeignKey(Source, blank=True, null=True, related_name="source4")
	source5 = models.ForeignKey(Source, blank=True, null=True, related_name="source5")
	
	codersnotes = models.TextField("Coder's Notes", blank=True, null=True,
		help_text="Notes from the Coder on these responses"
	)
	uncertainty = models.BooleanField(default=False)
	missing = models.BooleanField("Missing data", default=False)
	
	#to store page numbers. If you know a better way of doing this please change it
	page1 = models.CharField(max_length=256, blank=True, null=True)
	page2 = models.CharField(max_length=256, blank=True, null=True)
	page3 = models.CharField(max_length=256, blank=True, null=True)
	page4 = models.CharField(max_length=256, blank=True, null=True)
	page5 = models.CharField(max_length=256, blank=True, null=True)
	
	def __unicode__(self):
		if not self.pk:
			return u"Response: "
		elif hasattr(self, 'response'):
			return u"Response: {0}-{1}-{2}: {3}".format(self.question.id, self.culture_id, self.source1, self.response)
		else:
			return u"Response: {0}-{1}-{2}: NA".format(self.question.id, self.culture_id, self.source1)
			
	class Meta:
		db_table = 'responses'
		unique_together = ("question", "culture")


class IntegerResponse(Response):
	"""Saves Integer Values"""
	response = models.IntegerField(blank=True, null=True)
	
	class Meta:
		db_table = 'responses_integers'

	
class FloatResponse(Response):
	"""Saves Float Values"""
	response = models.FloatField(blank=True, null=True)

	class Meta:
		db_table = 'responses_floats'
	

class TextResponse(Response):
	"""Saves Text Values"""
	response = models.TextField(blank=True, null=True)

	class Meta:
		db_table = 'responses_texts'


class OptionResponse(Response):
	"""Saves Response Values"""
	response = models.CharField(max_length=3, blank=True, null=True)
	response_text = models.TextField(blank=True, null=True, 
		help_text="The text response from the user. We save this only for debugging purposes."
	)

	def save(self, *args, **kwargs):
		# override save to set response_text to correct value.
		if self.response:
			if hasattr(self.question, 'get_choice'):
			   self.response_text = self.question.get_choice(self.response)
		super(OptionResponse, self).save(*args, **kwargs)

	
	class Meta:
		db_table = 'responses_options'
	
statistic.register("Number of Questions", Question, graph=3)
statistic.register("Number of Responses", Response, graph=4)