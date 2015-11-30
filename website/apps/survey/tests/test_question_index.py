from django.test import TestCase

from website.apps.survey.tests.test_survey_section_edit import DataMixin


class Test_View_QuestionIndex(DataMixin, TestCase):
    """Tests the question-index view"""
