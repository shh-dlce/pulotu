from django.contrib import admin
import django.forms as forms
from reversion.admin import VersionAdmin
from website.apps.core.models import Source, Language, Culture, Section, Category, Glossary, Publication
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.template import Template, Context


class TrackedModelAdmin(admin.ModelAdmin):
	"""Mixin to automatically set editor field"""
	def add_view(self, request, form_url="", extra_context=None):
		data = request.GET.copy()
		data['editor'] = request.user.id
		request.GET = data
		return super(TrackedModelAdmin, self).add_view(request, form_url="", extra_context=extra_context)

class PublicationAdmin(TrackedModelAdmin, VersionAdmin):
	date_hierarchy='added'
	list_filter=('reference',)
class GlossaryAdmin(TrackedModelAdmin, VersionAdmin):
	date_hierarchy='added'
	list_filter=('term',)
	search_fields=('term', 'definition')

class LanguageAdmin(TrackedModelAdmin, VersionAdmin):
	
	date_hierarchy = 'added'
	list_filter = ('editor',)
	ordering = ('language', 'isocode')
	search_fields = ('isocode','language')
	
class SectionAdmin(TrackedModelAdmin, VersionAdmin):
	date_hierarchy = 'added'
	list_filter = ('editor',)
	search_fields = ('section',)

class CategoryAdmin(TrackedModelAdmin, VersionAdmin):
	date_hierarchy = 'added'
	search_fields=('category',)
	
class SourceAdmin(TrackedModelAdmin, VersionAdmin):
	date_hierarchy = 'added'
	list_filter = ('editor', 'author', 'year')
	ordering = ('author', 'year')
	prepopulated_fields = {'slug': ('author', 'year')}
	search_fields = ('author', 'year')
	

class CultureAdmin(TrackedModelAdmin, VersionAdmin):
	date_hierarchy = 'added'
	list_filter = ('editor',)
	ordering = ('culture',)
	prepopulated_fields = {'slug': ('culture',)}
	search_fields = ('culture',)
	filter_horizontal = ('languages',)
	
admin.site.register(Language, LanguageAdmin)
admin.site.register(Glossary, GlossaryAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Culture, CultureAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Publication, PublicationAdmin)
