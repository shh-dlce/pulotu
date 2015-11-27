from django import forms
from website.apps.core.models import Culture, Source, Language, Publication
from captcha.fields import CaptchaField
from django_select2 import *


class LanguageChoices(AutoModelSelect2MultipleField):
    queryset = Language.objects
    search_fields = ['language__icontains']


class CultureForm(forms.ModelForm):
    languages = LanguageChoices()

    class Meta:
        model = Culture
        exclude = ('id', 'editor', 'added', 'slug')
        widgets = {'languages': Select2MultipleWidget()}


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        exclude = ('id', 'editor', 'added', 'slug', 'bibtex')


class RegistrationForm(forms.Form):
    name = forms.CharField()
    affiliation = forms.CharField()
    email = forms.EmailField()
    reason = forms.CharField(label='Reason for requesting dataset', widget=forms.Textarea)
    captcha = CaptchaField()


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    comment = forms.CharField(label='Comments', widget=forms.Textarea)
    captcha = CaptchaField()


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        exclude = ('editor', 'slug')
