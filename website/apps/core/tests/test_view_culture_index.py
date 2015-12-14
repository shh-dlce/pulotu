from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from website.apps.core.models import Culture


class Test_CultureIndex(TestCase):
    """Tests the culture-index view"""

    def setUp(self):
        self.client = Client()
        self.url = reverse("culture-index")
        self.editor = User.objects.create(username='admin')
        self.culture1 = Culture.objects.create(
            culture='Maori',
            slug='maori',
            editor=self.editor)
        self.culture2 = Culture.objects.create(
            culture='English',
            slug='english',
            editor=self.editor)

    def test_index(self):
        response = self.client.get(self.url)
        self.assertContains(response, self.culture1.culture)
        self.assertContains(response, self.culture2.culture)
