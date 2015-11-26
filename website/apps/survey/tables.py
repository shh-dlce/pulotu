import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor

from website.apps.core.models import Culture, Section
from website.apps.core.tables import DataTable
from website.apps.survey.models import Question, Response

#class QuestionIndexTable(DataTable):
#	section = tables.Column()
#	number = tables.Column()
#	question = tables.LinkColumn('question-detail', args=[A('pk')])
#	count = tables.Column(verbose_name="Answered")

#	class Meta(DataTable.Meta):
#		model = Question
#		order_by = ('number',)
#		sequence = ('section', 'question', 'count', )
#		exclude = ('id', 'editor', 'added', 'response_type', 'information', 'polymorphic_ctype', 'number',)
#	Meta.attrs['summary'] = 'Table of Survey Questions'


class SurveyIndexTable(DataTable):
	culture = tables.LinkColumn('survey-culture-index', args=[A('slug')])
	qtodo = tables.Column(verbose_name="Questions To Answer")
	qdone = tables.Column(verbose_name="Questions Answered")
	qmissing = tables.Column(verbose_name="Missing Data")
	class Meta(DataTable.Meta):
		model = Culture
		order_by = ('culture',)
		sequence = ('culture', 'qtodo', 'qdone', 'qmissing')
		exclude = ('id', 'editor', 'added', 'slug', 'notes', 'languages', 'fact', 'ethonyms')
	Meta.attrs['summary'] = 'Table of Cultures'


class SurveyCultureIndexTable(DataTable):
	section = tables.LinkColumn('survey-section-edit', args=[A('culture.slug'), A('slug')])
	questions = tables.Column(verbose_name="Questions To Answer")
	toanswer = tables.Column(verbose_name="Questions Answered")
	qmissing = tables.Column(verbose_name="Missing Data")
	class Meta(DataTable.Meta):
		model = Section
		order_by = ('id',)
		sequence = ('section', 'questions', 'toanswer', 'qmissing')
		exclude = ('id', 'editor', 'added', 'slug', 'notes', 'culture', 'fact', 'number')
	Meta.attrs['summary'] = 'Table of Sections'


#class CultureResponsesTable(DataTable):
#	section = tables.Column()
#	number = tables.Column(verbose_name="Q.")
#	question = tables.Column()
#	response = tables.Column()
#	codersnotes = tables.Column(verbose_name="Notes")
	#source = tables.LinkColumn('source-detail', args=[A('source.slug')])
#	source=tables.Column()
#	uncertainty=tables.Column(verbose_name="Coder's Confidence")
#	class Meta(DataTable.Meta):
#		model = Response
#		order_by = ('number',)
#		sequence = ('section', 'question', 'response', 'source')
#		exclude = ('id', 'author', 'added', 'slug', 'notes', 'culture', 'polymorphic_ctype', 'number', 'codersnotes', 'source1', 'source2',
#			'source3', 'source4', 'source5', 'page1', 'page2', 'page3', 'page4', 'page5', 'missing')
#	Meta.attrs['summary'] = 'Table of Responses'


#class SourceResponsesTable(DataTable):
#	section = tables.Column()
#	number = tables.Column(verbose_name="Q.")
#	question = tables.Column()
#	response = tables.Column()
#	codersnotes = tables.Column(verbose_name="Notes")
#	culture = tables.LinkColumn('culture-detail', args=[A('culture.slug')])
#	uncertainty = tables.Column(verbose_name="Coder's Confidence")
	
#	class Meta(DataTable.Meta):
#		model = Response
#		order_by = ('number',)
#		sequence = ( 'section', 'culture', 'question', 'response', )
#		exclude = ('codersnotes', 'number','id', 'author', 'added', 'slug', 'notes', 'source', 'polymorphic_ctype',)
#	Meta.attrs['summary'] = 'Table of Responses'


#class QuestionResponsesTable(DataTable):
#	culture = tables.LinkColumn('culture-detail', args=[A('culture.slug')])
#	source = tables.Column()
#	response = tables.Column()
#	uncertainty=tables.Column(verbose_name="Coder's Confidence")

#	class Meta(DataTable.Meta):
#		model = Response
#		order_by = ('culture',)
#		sequence = ('culture', 'response','source', )
#		exclude = ('id', 'author', 'added', 'codersnotes', 'polymorphic_ctype', )
#	Meta.attrs['summary'] = 'Table of Responses'
