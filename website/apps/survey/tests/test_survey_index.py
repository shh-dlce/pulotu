from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from website.apps.core.models import Culture


class Test_View_SurveyIndex_NotLoggedIn(TestCase):
    """Tests the survey_index view"""
    def setUp(self):
        self.client = Client()
        self.editor = User.objects.create_user('admin',
                                               'admin@example.com', "test")
        self.culture1 = Culture.objects.create(culture='Maori', 
                                    slug='maori',editor=self.editor)
        self.culture2 = Culture.objects.create(culture='English', 
                                    slug='english', editor=self.editor)
        self.url = reverse("survey-index")

    
    def test_error_when_not_logged_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, 
                             "/accounts/login/?next=%s" % self.url, 
                             status_code=302, 
                             target_status_code=200)


class Test_View_SurveyIndex_LoggedIn(TestCase):
    """Tests the survey_index view"""
    def setUp(self):
        self.editor = User.objects.create_user('admin',
                                               'admin@example.com', "test")
        self.culture1 = Culture.objects.create(culture='Maori', 
                                    slug='maori',editor=self.editor)
        self.culture2 = Culture.objects.create(culture='English', 
                                    slug='english', editor=self.editor)
        self.client = Client()
        self.client.login(username="admin", password="test")
        self.url = reverse("survey-index")

    def test_index(self):
        response = self.client.get(self.url)
        self.assertContains(response, self.culture1.culture)
        self.assertContains(response, self.culture2.culture)
    