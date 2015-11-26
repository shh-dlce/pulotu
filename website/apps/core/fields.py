from django import forms

from django_select2 import *

from website.apps.core.models import Source


class SourceField(AutoModelSelect2Field):
	queryset = Source.objects
	search_fields = ['source__icontains',]
	def get_model_field_values(self, value):
		return {'source': value}