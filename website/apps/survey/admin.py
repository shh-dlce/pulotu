import django.forms as forms

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.contrib import admin
from polymorphic.admin import (
    PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter,
)
from reversion.admin import VersionAdmin
from website.apps.core.admin import TrackedModelAdmin
from website.apps.survey.models import Question, OptionQuestion, Section
from website.apps.survey.models import (
    Response, OptionResponse, FloatResponse, IntegerResponse, TextResponse,
)
from django.template import Template, Context


# Questions
class QuestionChildAdmin(TrackedModelAdmin, VersionAdmin, PolymorphicChildModelAdmin):
    base_model = Question


class QuestionAdmin(TrackedModelAdmin, VersionAdmin, PolymorphicParentModelAdmin):
    actions = ['changeCategory', 'questionNumber']
    base_model = Question
    list_filter = (PolymorphicChildModelFilter,)
    ordering = ('number',)
    child_models = [
        (Question, QuestionChildAdmin),
        (OptionQuestion, QuestionChildAdmin),
    ]
    changeSuccess = Template('Successfully changed question numbers') 
    
    class NumberForm(forms.Form):
        _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
        offset = forms.IntegerField()

    def questionNumber(self, request, queryset):
        form = None
        if 'cancel' in request.POST:
            self.message_user(request, 'Canceled changing question number')
            return
        elif 'change' in request.POST:
            form = self.NumberForm(request.POST)
            if form.is_valid():
                offset = form.cleaned_data['offset']
                for link in queryset:
                    link.number += offset
                    link.save()
                self.message_user(
                    request,
                    self.changeSuccess.render(Context({'count': queryset.count()})))
                return HttpResponseRedirect(request.get_full_path())
        if not form:
            form = self.NumberForm(
                initial={
                    '_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
        return render_to_response(
            'admin/categorize.html',
            RequestContext(
                request,
                {'links': queryset, 'form': form, 'path': request.get_full_path()}))

    questionNumber.short_description = 'Change question number(s)' 
    
    categorySuccess = Template('Successfully changed section(s) and subsection(s)')

    class CategoryForm(forms.Form):
        _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
        section = forms.ModelChoiceField(Section.objects)
        subsection = forms.ModelChoiceField(Section.objects)

    def changeCategory(self, request, queryset):
        form = None
        if 'cancel' in request.POST:
            self.message_user(request, 'Canceled change section(s)')
            return
        elif 'change' in request.POST:
            # do the categorization
            form = self.CategoryForm(request.POST)
            if form.is_valid():
                section = form.cleaned_data['section']
                subsection = form.cleaned_data['subsection']
                for link in queryset:
                    link.subsection = section
                    link.section = subsection
                    link.save()
                self.message_user(
                    request,
                    self.categorySuccess.render(
                        Context({'count': queryset.count(), 'category': section})))
                return HttpResponseRedirect(request.get_full_path())
        if not form:
            form = self.CategoryForm(
                initial={
                    '_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
        return render_to_response(
            'admin/change.html',
            RequestContext(
                request,
                {'links': queryset, 'form': form, 'path': request.get_full_path()}))

    changeCategory.short_description = 'Change section' 

    
# Responses.
class ResponseAdmin(TrackedModelAdmin, VersionAdmin):
    date_hierarchy = 'added'
    list_filter = ('author', 'question', 'culture')
    ordering = ('id',)
    search_fields = ('codersnotes',)
    list_display = ('question', 'culture', 'author')
    

class FloatResposeAdmin(TrackedModelAdmin, VersionAdmin):
    date_hierarchy = 'added'
    list_filter = ('author', 'question', 'culture')
    ordering = ('id',)
    search_fields = ('codersnotes',)
    list_display = ('question', 'culture', 'author', 'response')


class IntegerResponseAdmin(TrackedModelAdmin, VersionAdmin):
    date_hierarchy = 'added'
    list_filter = ('author', 'question', 'culture')
    ordering = ('id',)
    search_fields = ('codersnotes',)
    list_display = ('question', 'culture', 'author', 'response')


class TextResponseAdmin(TrackedModelAdmin, VersionAdmin):
    date_hierarchy = 'added'
    list_filter = ('author', 'question', 'culture')
    ordering = ('id',)
    search_fields = ('codersnotes',)
    list_display = ('question', 'culture', 'author', 'response')


class OptionResponseAdmin(TrackedModelAdmin, VersionAdmin):
    date_hierarchy = 'added'
    list_filter = ('author', 'question', 'culture')
    ordering = ('id',)
    search_fields = ('codersnotes',)
    list_display = ('question', 'culture', 'author', 'response')
 

admin.site.register(Response, ResponseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(FloatResponse, FloatResposeAdmin)
admin.site.register(IntegerResponse, IntegerResponseAdmin)
admin.site.register(TextResponse, TextResponseAdmin)
admin.site.register(OptionResponse, OptionResponseAdmin)
