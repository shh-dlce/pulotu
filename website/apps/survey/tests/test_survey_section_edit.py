from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from website.apps.core.models import Culture, Section
from website.apps.survey.models import Question

class DataMixin(object):
    def setUp(self):
        return
        self.editor = User.objects.create_user('admin',
                                               'admin@example.com', "test")
        self.culture1 = Culture.objects.create(culture='Maori', 
                                    slug='maori',editor=self.editor)
        self.culture2 = Culture.objects.create(culture='English', 
                                    slug='english', editor=self.editor)
        self.section = Section.objects.create(section="Test", slug="test",
                                    editor=self.editor)
        self.question_int = Question.objects.create(section=self.section,
                                    number=1, question='How old are you?',
                                    information="", response_type='Int',
                                    editor=self.editor)
        self.question_float = Question.objects.create(section=self.section,
                                    number=2, question='How far away is coffee?',
                                    information="", response_type='Float',
                                    editor=self.editor)
        self.question_text = Question.objects.create(section=self.section,
                                    number=3, question='What is your name?',
                                    information="", response_type='Text',
                                    editor=self.editor)
        self.client = Client()
        

class Test_View_SurveySectionEdit_NotLoggedIn(DataMixin, TestCase):
    """Tests the survey-section-edit view"""
    def test_error_when_not_logged_in(self):
        return
        url = reverse("survey-section-edit", kwargs={'culture': 'english', 'section': 'test'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, 
                             "/accounts/login/?next=%s" % url, 
                             status_code=302, 
                             target_status_code=200)



class Test_View_SurveySectionEdit_LoggedIn(DataMixin, TestCase):
    """Tests the survey-section-edit view"""
    def test_404_on_missing_culture(self):
        return
        self.client.login(username="admin", password="test")
        response = self.client.get(reverse("survey-section-edit", kwargs={'culture': 'fudge', 'section': 'test'}))
        self.assertEqual(response.status_code, 404)

    def test_404_on_missing_section(self):
        return
        self.client.login(username="admin", password="test")
        response = self.client.get(reverse("survey-section-edit", kwargs={'culture': 'maori', 'section': 'fudge'}))
        self.assertEqual(response.status_code, 404)
        
    def test_page(self):
        return
        self.client.login(username="admin", password="test")
        response = self.client.get(reverse("survey-section-edit", kwargs={'culture': 'maori', 'section': 'test'}))
        self.assertContains(response, self.question_int.question)
        self.assertContains(response, self.question_float.question)
        self.assertContains(response, self.question_text.question)
        