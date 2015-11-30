# coding: utf8
from __future__ import unicode_literals
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from website.apps.core.models import Culture, Source, Section, Language, Category
from website.apps.survey.models import (
    OptionQuestion, TextResponse, FloatResponse, Question,
)


class WithEditor(TestCase):
    def setUp(self):
        self.client = Client()
        self.editor = User.objects.create_user('admin', 'admin@example.com', "test")

    def object(self, cls, **kw):
        kw.setdefault('editor', self.editor)
        return cls.objects.create(**kw)

    def login(self, username="admin", password="test"):
        self.client.login(username=username, password=password)


class WithCompleteDatabase(WithEditor):
    """Base class for tests requiring a minimal yet complete database."""

    def setUp(self):
        WithEditor.setUp(self)
        self.culture1 = self.object(
            Culture,
            culture='Maori',
            slug='maori')
        lang = self.object(
            Language,
            language='lname',
            isocode='abc',
            abvdcode=5)
        self.culture1.languages.add(lang)
        self.culture2 = self.object(
            Culture,
            culture='English',
            slug='english')
        self.source = self.object(
            Source,
            year=1991,
            author='Smith',
            slug='Smith1991',
            reference='S2',
            comment='c1')
        cat = self.object(
            Category,
            id=1,
            category='cat 1',
            number=1)
        self.section = self.object(
            Section,
            section="Test",
            category=cat,
            slug="test")
        self.subsection = self.object(
            Section,
            section="Sub",
            category=cat,
            slug="sub")
        self.question = self.object(
            OptionQuestion,
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
            information="..")
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
        lat = self.object(
            Question,
            id=2,
            section=self.section,
            subsection=self.subsection,
            number=2,
            question='Latitude',
            simplified_question='Latitude',
            displayPublic=False,
            information="..")
        FloatResponse.objects.create(
            question=lat,
            culture=self.culture1,
            codersnotes='',
            author=self.editor,
            source1=self.source,
            response=5.5)
        lon = self.object(
            Question,
            id=3,
            section=self.section,
            subsection=self.subsection,
            number=3,
            question='Longitude',
            simplified_question='Longitude',
            displayPublic=False,
            information="..")
        FloatResponse.objects.create(
            question=lon,
            culture=self.culture1,
            codersnotes='',
            author=self.editor,
            source1=self.source,
            response=-5.5)
