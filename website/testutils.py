# coding: utf8
from __future__ import unicode_literals
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from website.apps.core.models import Culture, Source, Section, Language, Category
from website.apps.survey.models import (
    OptionQuestion, TextResponse, FloatResponse, Question,
)


class WithCompleteDatabase(TestCase):
    """Base class for tests requiring a minimal yet complete database."""

    def setUp(self):
        self.client = Client()
        self.editor = User.objects.create_user('admin', 'admin@example.com', "test")
        self.culture1 = Culture.objects.create(
            culture='Maori',
            slug='maori',
            editor=self.editor)
        lang = Language.objects.create(
            language='lname',
            isocode='abc',
            abvdcode=5,
            editor=self.editor)
        self.culture1.languages.add(lang)
        self.culture2 = Culture.objects.create(
            culture='English',
            slug='english',
            editor=self.editor)
        self.source = Source.objects.create(
            year=1991, author='Smith',
            slug='Smith1991', reference='S2',
            comment='c1', editor=self.editor)
        cat = Category.objects.create(
            id=1,
            category='cat 1',
            number=1,
            editor=self.editor)
        self.section = Section.objects.create(
            section="Test",
            category=cat,
            slug="test",
            editor=self.editor)
        self.subsection = Section.objects.create(
            section="Sub", slug="sub",
            editor=self.editor)
        self.question = OptionQuestion.objects.create(
            id=1,
            section=self.section,
            subsection=self.subsection,
            number=1,
            question='Where are you?',
            simplified_question='where',
            options="""
(?) Missing data
(0) Low
(1) Moderate
(2) High
""",
            information="..",
            editor=self.editor)
        self.response = TextResponse.objects.create(
            question=self.question,
            culture=self.culture1,
            codersnotes='',
            author=self.editor,
            source1=self.source,
            source2=self.source,
            source3=self.source,
            source4=self.source,
            source5=self.source,
            response='Low')

        lat = Question.objects.create(
            id=2,
            section=self.section,
            subsection=self.subsection,
            number=2,
            question='Latitude',
            simplified_question='Latitude',
            displayPublic=False,
            information="..",
            editor=self.editor)
        FloatResponse.objects.create(
            question=lat,
            culture=self.culture1,
            codersnotes='',
            author=self.editor,
            source1=self.source,
            response=5.5)
        lon = Question.objects.create(
            id=3,
            section=self.section,
            subsection=self.subsection,
            number=3,
            question='Longitude',
            simplified_question='Longitude',
            displayPublic=False,
            information="..",
            editor=self.editor)
        FloatResponse.objects.create(
            question=lon,
            culture=self.culture1,
            codersnotes='',
            author=self.editor,
            source1=self.source,
            response=-5.5)
