from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

class Test_Robots_Txt(TestCase):
    """Tests the robots.txt page"""
    
    def setUp(self):
        self.client = Client()
        self.url = reverse("robots_txt")

    def test_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'robots.txt')
    
    def test_content(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'User-agent')
        
        
