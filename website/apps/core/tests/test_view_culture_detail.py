from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from website.apps.core.models import Culture


class Test_CultureIndex(TestCase):
    """Tests the culture-detail view"""
    
    def setUp(self):
        self.client = Client()
        self.editor = User.objects.create(username='admin')
        self.culture1 = Culture.objects.create(culture='Maori', 
                                    slug='maori',editor=self.editor)
        self.culture2 = Culture.objects.create(culture='English', 
                                    slug='english', editor=self.editor)
        
    def test_404_on_missing_culture(self):
        url = reverse("culture-detail", kwargs={'slug': 'fudge'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_find_valid_culture(self):
        url = reverse("culture-detail", kwargs={'slug': 'maori'})
        response = self.client.get(url)
        self.assertContains(response, 'Maori')
        url = reverse("culture-detail", kwargs={'slug': 'english'})
        response = self.client.get(url)
        self.assertContains(response, 'English')
    
    def test_has_responses(self):
        url = reverse("culture-detail", kwargs={'slug': 'maori'})
        response = self.client.get(url)
        assert 'table' in response.context