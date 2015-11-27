import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor

from website.apps.core.models import Source, Culture, Language

# Note, due to the current version of django_tables2 not merging in Meta classes
# https://github.com/bradleyayers/django-tables2/issues/85
# The work around is to inherit class Meta in the subclasses e.g.
# class Child(DataTable):
#     class Meta(DataTable.Meta):
#         pass
#
# another annoyance is that you can't override anything in Meta - it'll cause a 
# NameError to be raised. The work around is this:
#
# class Child(DataTable):
#     class Meta(DataTable.Meta):
#         pass
#     Meta.var = X
#
# Ugly, but it works.


class DataTable(tables.Table):
    """Parent class for Datatables"""
    class Meta:
        orderable = True
        default = u''
        attrs = {
            'class': "table table-bordered table-condensed",
            'summary': '',
        }
    

class SourceIndexTable(DataTable):
    """Source Listing"""
    author = tables.LinkColumn('source-detail', args=[A('slug')])
    reference = tables.LinkColumn('source-detail', args=[A('slug')])
    count = tables.LinkColumn('source-detail', args=[A('slug')])
    
    class Meta(DataTable.Meta):
        model = Source
        exclude = ('id', 'editor', 'added', 'slug', 'comment', 'bibtex')
    Meta.attrs['summary'] = 'Table of Sources'
    

class CultureIndexTable(DataTable):
    """Culture Listing"""
    culture = tables.LinkColumn('culture-detail', args=[A('slug')])
    
    class Meta(DataTable.Meta):
        model = Culture
        order_by = ('culture',)
        sequence = ('culture',)
        exclude = ('id', 'editor', 'added', 'slug', 'notes', 'languages')
    Meta.attrs['summary'] = 'Table of Cultures'
    
    
class LanguageIndexTable(DataTable):
    """Language Listing"""
    language = tables.LinkColumn('language-detail', args=[A('isocode')])
    isocode = tables.LinkColumn('language-detail', args=[A('isocode')])
    
    class Meta(DataTable.Meta):
        model = Language
        order_by = ('language',)
        sequence = ('isocode', 'language', 'classification', 'abvdcode',)
        exclude = ('id', 'editor', 'added', 'slug', 'notes',)
    Meta.attrs['summary'] = 'Table of Languages'
