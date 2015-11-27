from django import forms
from website.apps.survey.models import Question
from website.apps.survey.models import (
    Response, IntegerResponse, FloatResponse, TextResponse, OptionResponse,
)
from django_select2 import *


class ExportForm(forms.Form):
    questions = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
    exportinfo = forms.CharField()


class ResponseForm(forms.ModelForm):
    # WARNING - this form does NOT allow you to edit the culture or the question!
    def __init__(self, *args, **kwargs):
        super(ResponseForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        self.fields['question'].widget.attrs['readonly'] = True
        self.fields['culture'].widget.attrs['readonly'] = True
    
    def clean_culture(self):
        return self.initial['culture']
    
    def clean_question(self):
        return self.initial['question']
        
    class Meta:
        model = Response 
        hidden = ('question', 'culture')
        exclude = ('id', 'author', 'added',)


# it seems that inheritence of exclude etc doesn't work, damn it. 
# so, have to define it for each form
class IntegerResponseForm(ResponseForm):
    response = forms.IntegerField(required=False)
    missing = forms.BooleanField(required=False)

    class Meta:
        model = IntegerResponse
        hidden = ('id', 'question', 'culture')
        exclude = ('author', 'added',)
        widgets = {
            'question': forms.widgets.HiddenInput(),
            'culture': forms.widgets.HiddenInput(),
            'response': forms.widgets.TextInput(attrs={'class': 'span6', 'rows': '3'}),
            'codersnotes': forms.widgets.Textarea(attrs={'class': 'span6', 'rows': '3'}),
        }
    
    # to validate the form
    def clean(self):
        cleaned_data = super(IntegerResponseForm, self).clean()
        response = cleaned_data.get("response")
        missing = cleaned_data.get("missing")
        source1 = cleaned_data.get("source1")
        if response == 0 and source1:
            return cleaned_data
        elif response == 0 and not source1:
            raise forms.ValidationError("Source 1 is a required field.")
        
        if not missing and not response: #if no response and not missing data
            raise forms.ValidationError("Response is a required field.")
        if response and not source1: #if response and no source
            raise forms.ValidationError("Source 1 is a required field.")
        return cleaned_data

        
class FloatResponseForm(ResponseForm):
    response = forms.FloatField(required=False)
    missing = forms.BooleanField(required=False)

    class Meta:
        model = FloatResponse
        hidden = ('id', 'question', 'culture')
        exclude = ('author', 'added',)
        widgets = {
            'question': forms.widgets.HiddenInput(),
            'culture': forms.widgets.HiddenInput(),
            'response': forms.widgets.TextInput(attrs={'class': 'span6', 'rows': '3'}),
            'codersnotes': forms.widgets.Textarea(attrs={'class': 'span6', 'rows': '3'}),
            'source1': forms.widgets.Select(attrs={'class': 'sourceSelect'}),
        }

    def clean(self):
        cleaned_data = super(FloatResponseForm, self).clean()
        response = cleaned_data.get("response")
        missing = cleaned_data.get("missing")
        source1 = cleaned_data.get("source1")
        if response == 0 and source1:
            return cleaned_data
        elif response == 0 and not source1:
            raise forms.ValidationError("Source 1 is a required field.")
        elif not missing and not response:
            raise forms.ValidationError("Response is a required field.")
        elif response and not source1:
            raise forms.ValidationError("Source 1 is a required field.")
        return cleaned_data


class TextResponseForm(ResponseForm):
    response = forms.CharField(
        required=False,
        widget=forms.widgets.Textarea(attrs={'class': 'span6', 'rows': '3'}))
    missing = forms.BooleanField(required=False)

    class Meta:
        model = TextResponse
        hidden = ('id', 'question', 'culture')
        exclude = ('author', 'added',)
        widgets = {
            'question': forms.widgets.HiddenInput(),
            'culture': forms.widgets.HiddenInput(),
            'response': forms.widgets.Textarea(attrs={'class': 'span6', 'rows': '3'}),
            'codersnotes': forms.widgets.Textarea(attrs={'class': 'span6', 'rows': '3'}),
        }

    def clean(self):
        cleaned_data = super(TextResponseForm, self).clean()
        response = cleaned_data.get("response")
        missing = cleaned_data.get("missing")
        source1 = cleaned_data.get("source1")
        if not missing and not response:
            raise forms.ValidationError("Response is a required field.")
        elif response and not source1:
            raise forms.ValidationError("Source 1 is a required field.")
        return cleaned_data


class OptionResponseForm(ResponseForm):
    response = forms.ChoiceField(
        required=False, choices=(), widget=forms.RadioSelect(attrs={'class': 'radios'}),)
    
    class Meta:
        model = OptionResponse
        hidden = ('id', 'question', 'culture')
        exclude = ('author', 'added',)
        widgets = {
            'question': forms.widgets.HiddenInput(),
            'culture': forms.widgets.HiddenInput(),
            'response': forms.widgets.Textarea(attrs={'class': 'span6', 'rows': '3'}),
            'codersnotes': forms.widgets.Textarea(attrs={'class': 'span6', 'rows': '3'}),
        }

    # to validate data
    def clean(self):
        cleaned_data = super(OptionResponseForm, self).clean()
        response = cleaned_data.get("response")
        source1 = cleaned_data.get("source1")
        missing = cleaned_data.get("missing")
        
        # if both missing data and response are chosen the form will be validated and
        # in views.py, response is saved as '?'
        if not response and not missing:  # if no response is given, raise an error
            raise forms.ValidationError("Response is a required field.")
        if not missing and response and not source1:
            # if response is given and no source is given
            raise forms.ValidationError("Source 1 is a required field.")
        return cleaned_data


def get_response_type(response_type=None):
    """Returns the correct Response model type for the given field type"""
    # I could do this more elegantly by getattr and instantiating based on 
    # the stored value, but this way gives me top down control and a bit of 
    # safety
    if response_type is None:
        return Response
    elif response_type == Question.RESPONSETYPE_INTEGER:
        return IntegerResponse
    elif response_type == Question.RESPONSETYPE_FLOAT:
        return FloatResponse
    elif response_type == Question.RESPONSETYPE_TEXT:
        return TextResponse
    elif response_type == Question.RESPONSETYPE_OPTION:
        return OptionResponse
    else:
        raise ValueError("Unknown Response Type: {0}".format(response_type))


def get_form_type(response_type=None):
    """Returns the correct Response form type for the given field type"""
    # I could do this more elegantly by getattr and instantiating based on 
    # the stored value, but this way gives me top down control and a bit of 
    # safety
    if response_type is None:
        return ResponseForm
    elif response_type == Question.RESPONSETYPE_INTEGER:
        return IntegerResponseForm
    elif response_type == Question.RESPONSETYPE_FLOAT:
        return FloatResponseForm
    elif response_type == Question.RESPONSETYPE_TEXT:
        return TextResponseForm
    elif response_type == Question.RESPONSETYPE_OPTION:
        return OptionResponseForm
    else:
        raise ValueError("Unknown Response Type: {0}".format(response_type))


def construct_section_forms(post_data=None, culture_obj=None, section_obj=None):
    """Constructs a form for the given culture, section, with the specified post data"""
    # get all questions for the section and culture.
    assert culture_obj is not None, "culture object cannot be None."
    assert section_obj is not None, "section object cannot be None."
    
    forms = []
    
    # get all existing Responses
    responses = {}
    source1 = {}
    for r in Response.objects.all().filter(
            culture=culture_obj, question__section=section_obj):
        responses[r.question_id] = r
        source1[r.question_id] = r.source1
    # loop over questions in this section and inject with existing 
    # responses & post data
    for q in Question.objects.all().order_by('number').filter(section=section_obj):
        rtype = get_response_type(q.response_type)
        formtype = get_form_type(q.response_type)
        # manuipulate response to constrain cultures/questions
        resp = responses.get(q.id, None)
        s = source1.get(q.id, None)
        if resp is not None:
            resp.culture = culture_obj
            resp.question = q
            resp.source1 = s

        # create a form, injecting POST data 
        form = formtype(
            post_data,
            instance=resp,
            initial={'culture': culture_obj, 'question': q},
            prefix=q.id
        )
        # add correct choices for OptionForms
        if formtype == OptionResponseForm:
            form.fields['response'].choices = q.get_choices(with_empty=True)
        
        # add these here so I can get them in the template.
        form.qnumber = q.number
        form.qinformation = q.information
        form.qtext = q.question
        form.qresponsetype = q.response_type
        forms.append(form)
    return forms
