import django.forms as forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.contrib import admin
from django.template import Template, Context
from polymorphic.admin import (
    PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter,
)
from reversion.admin import VersionAdmin
from website.apps.core.admin import TrackedModelAdmin
from website.apps.survey.models import Question, OptionQuestion, Section
from website.apps.survey.models import (
    Response, OptionResponse, FloatResponse, IntegerResponse, TextResponse,
)


class QuestionChildAdmin(TrackedModelAdmin, VersionAdmin, PolymorphicChildModelAdmin):
    base_model = Question


class CategoryForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    section = forms.ModelChoiceField(Section.objects)
    subsection = forms.ModelChoiceField(Section.objects)


def change_category(request, queryset, message_user):
    form = None
    if 'cancel' in request.POST:
        message_user(request, 'Canceled change section(s)')
        return
    elif 'change' in request.POST:
        # do the categorization
        form = CategoryForm(request.POST)
        if form.is_valid():
            section = form.cleaned_data['section']
            subsection = form.cleaned_data['subsection']
            for link in queryset:
                link.subsection = section
                link.section = subsection
                link.save()
            message_user(
                request,
                Template('Successfully changed section(s) and subsection(s)').render(
                    Context({'count': queryset.count(), 'category': section})))
            return HttpResponseRedirect(request.get_full_path())
    if not form:
        form = CategoryForm(
            initial={
                '_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
    return render_to_response(
        'admin/change.html',
        RequestContext(
            request,
            {'links': queryset, 'form': form, 'path': request.get_full_path()}))


class NumberForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    offset = forms.IntegerField()


def question_number(request, queryset, message_user):
    form = None
    if 'cancel' in request.POST:
        message_user(request, 'Canceled changing question number')
        return
    elif 'change' in request.POST:
        form = NumberForm(request.POST)
        if form.is_valid():
            offset = form.cleaned_data['offset']
            for link in queryset:
                link.number += offset
                link.save()
            message_user(
                request,
                Template('Successfully changed question numbers').render(
                    Context({'count': queryset.count()})))
            return HttpResponseRedirect(request.get_full_path())
    if not form:
        form = NumberForm(
            initial={
                '_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
    return render_to_response(
        'admin/categorize.html',
        RequestContext(
            request,
            {'links': queryset, 'form': form, 'path': request.get_full_path()}))


class QuestionAdmin(TrackedModelAdmin, VersionAdmin, PolymorphicParentModelAdmin):
    actions = ['changeCategory', 'questionNumber']
    base_model = Question
    list_filter = (PolymorphicChildModelFilter,)
    ordering = ('number',)
    child_models = [
        (Question, QuestionChildAdmin),
        (OptionQuestion, QuestionChildAdmin),
    ]

    def questionNumber(self, request, queryset):  # pragma: no cover
        return question_number(request, queryset, self.message_user)

    questionNumber.short_description = 'Change question number(s)'

    def changeCategory(self, request, queryset):  # pragma: no cover
        return change_category(request, queryset, self.message_user)

    changeCategory.short_description = 'Change section'


class ResponseAdmin(TrackedModelAdmin, VersionAdmin):
    date_hierarchy = 'added'
    list_filter = ('author', 'question', 'culture')
    ordering = ('id',)
    search_fields = ('codersnotes',)
    list_display = ('question', 'culture', 'author')


class FloatResponseAdmin(TrackedModelAdmin, VersionAdmin):
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
admin.site.register(FloatResponse, FloatResponseAdmin)
admin.site.register(IntegerResponse, IntegerResponseAdmin)
admin.site.register(TextResponse, TextResponseAdmin)
admin.site.register(OptionResponse, OptionResponseAdmin)
