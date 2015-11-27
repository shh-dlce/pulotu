import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor

from website.apps.core.models import Culture, Section
from website.apps.core.tables import DataTable


class SurveyIndexTable(DataTable):
    culture = tables.LinkColumn('survey-culture-index', args=[A('slug')])
    qtodo = tables.Column(verbose_name="Questions To Answer")
    qdone = tables.Column(verbose_name="Questions Answered")
    qmissing = tables.Column(verbose_name="Missing Data")

    class Meta(DataTable.Meta):
        model = Culture
        order_by = ('culture',)
        sequence = ('culture', 'qtodo', 'qdone', 'qmissing')
        exclude = (
            'id', 'editor', 'added', 'slug', 'notes', 'languages', 'fact', 'ethonyms')
    Meta.attrs['summary'] = 'Table of Cultures'


class SurveyCultureIndexTable(DataTable):
    section = tables.LinkColumn(
        'survey-section-edit', args=[A('culture.slug'), A('slug')])
    questions = tables.Column(verbose_name="Questions To Answer")
    toanswer = tables.Column(verbose_name="Questions Answered")
    qmissing = tables.Column(verbose_name="Missing Data")

    class Meta(DataTable.Meta):
        model = Section
        order_by = ('id',)
        sequence = ('section', 'questions', 'toanswer', 'qmissing')
        exclude = ('id', 'editor', 'added', 'slug', 'notes', 'culture', 'fact', 'number')
    Meta.attrs['summary'] = 'Table of Sections'
