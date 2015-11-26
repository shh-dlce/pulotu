from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from website.apps.core.models import Culture, Section
from website.apps.survey.models import Question

from website.apps.survey.tests.test_survey_section_edit import DataMixin

class Test_View_QuestionIndex(DataMixin, TestCase):
    """Tests the question-index view"""
    def test_index(self):
        response = self.client.get(reverse('question-index'))
        self.assertContains(response, self.question_int.question)
        self.assertContains(response, self.question_float.question)
        self.assertContains(response, self.question_text.question)
