from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from website.apps.core.models import Culture, Source, Section
from website.apps.survey.models import Question, Response, IntegerResponse, FloatResponse, \
    TextResponse


class Test_QuestionDetail(TestCase):
    """Tests the question-detail view"""

    def setUp(self):
        self.client = Client()
        self.editor = User.objects.create(username='admin')
        self.culture1 = Culture.objects.create(
            culture='Maori',
            slug='maori',
            editor=self.editor)
        self.culture2 = Culture.objects.create(
            culture='English',
            slug='english',
            editor=self.editor)
        self.section_one = Section.objects.create(
            section="Test",
            slug="test",
            editor=self.editor)
        self.section_two = Section.objects.create(
            section="Example",
            slug="example",
            editor=self.editor)
        self.subsection = Section.objects.create(
            section="Sub",
            slug="sub",
            editor=self.editor)
        self.question_int = Question.objects.create(
            section=self.section_one,
            subsection=self.subsection,
            number=1,
            question='How old are you?',
            information="",
            response_type='Int',
            editor=self.editor)
        self.question_float = Question.objects.create(
            section=self.section_one,
            subsection=self.subsection,
            number=2,
            question='How far away is coffee?',
            information="",
            response_type='Float',
            editor=self.editor)
        self.question_text = Question.objects.create(
            section=self.section_two,
            subsection=self.subsection,
            number=3,
            question='What is your name?',
            information="",
            response_type='Text',
            editor=self.editor)
        self.source = Source.objects.create(
            year=1991,
            author='Smith',
            slug='Smith1991',
            reference='S2',
            comment='c1',
            editor=self.editor)

    def test_404_on_missing_question(self):
        return
        url = reverse("question-detail", kwargs={'pk': 1000})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_find_valid_question(self):
        return
        url = reverse("question-detail", kwargs={'pk': self.question_int.id})
        response = self.client.get(url)
        self.assertContains(response, self.question_int.question)

        url = reverse("question-detail", kwargs={'pk': self.question_float.id})
        response = self.client.get(url)
        self.assertContains(response, self.question_float.question)

        url = reverse("question-detail", kwargs={'pk': self.question_text.id})
        response = self.client.get(url)
        self.assertContains(response, self.question_text.question)

    def test_has_responses(self):
        resp = TextResponse.objects.create(
            author=self.editor,
            question=self.question_text,
            culture=self.culture1,
            source1=self.source,
            codersnotes="",
            response='FUDGE',
        )
        resp.save()
        return
        url = reverse("question-detail", kwargs={'pk': self.question_text.id})
        response = self.client.get(url)
        assert 'table' in response.context
        assert "FUDGE" in response.content
