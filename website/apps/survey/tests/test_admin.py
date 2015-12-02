# coding: utf8
from __future__ import unicode_literals

from website.apps.survey.models import Question
from website.apps.survey.admin import change_category, question_number
from website.testutils import WithCompleteDatabase


class MockPOST(dict):
    def getlist(self, name):
        return []


class MockRequest(object):
    def __init__(self, **kw):
        self.POST = MockPOST(kw)
        self.META = {}

    def get_full_path(self):
        return '/testing'


class Message(object):
    def __init__(self):
        self.msg = None

    def __call__(self, req, msg):
        self.msg = msg


class Tests(WithCompleteDatabase):
    def setUp(self):
        WithCompleteDatabase.setUp(self)
        self.msg = Message()
        self.selected = Question.objects.all().values_list('id', flat=True)

    def test_change_category(self):
        res = change_category(MockRequest(), Question.objects.all(), self.msg)
        self.assertEquals(res.status_code, 200)

    def test_change_category_cancel(self):
        change_category(
            MockRequest(
                action='test_changeCategory',
                _selected_action=self.selected,
                cancel=True),
            Question.objects.all(),
            self.msg)
        self.assertIn('Canceled', self.msg.msg)

    def test_change_category_change(self):
        change_category(
            MockRequest(
                action='test_changeCategory',
                _selected_action=self.selected,
                section=self.section.id,
                subsection=self.subsection.id,
                change=True),
            Question.objects.all(),
            self.msg)
        self.assertIn('Successfully', self.msg.msg)

    def test_question_number(self):
        res = question_number(MockRequest(), Question.objects.all(), self.msg)
        self.assertEquals(res.status_code, 200)

    def test_question_number_cancel(self):
        question_number(
            MockRequest(
                action='test_changeCategory',
                _selected_action=self.selected,
                cancel=True),
            Question.objects.all(),
            self.msg)
        self.assertIn('Canceled', self.msg.msg)

    def test_question_number_change(self):
        question_number(
            MockRequest(
                action='test_changeCategory',
                _selected_action=self.selected,
                offset=5,
                change=True),
            Question.objects.all(),
            self.msg)
        self.assertIn('Successfully', self.msg.msg)
