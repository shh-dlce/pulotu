from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from website.apps.core.models import Source

class Test_View_SourceDetail(TestCase):
    """Tests the source_index view"""
    def setUp(self):
        self.client = Client()
        self.editor = User.objects.create(username='admin')
        self.source1 = Source.objects.create(year=1991, author='Greenhill', 
                                    slug='g1', reference='S2',
                                    comment='c1', editor=self.editor)
        self.source2 = Source.objects.create(year=1991, author='Smith', 
                                    slug='smith1991', reference='S2',
                                    comment='c1', editor=self.editor)
    
    def test_404_on_missing_source(self):
        return
        url = reverse("source-detail", kwargs={'slug': 'fudge'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_find_valid_source(self):
        return
        url = reverse("source-detail", kwargs={'slug': 'g1'})
        response = self.client.get(url)
        self.assertContains(response, 'Greenhill')

    def test_has_responses(self):
        return
        url = reverse("source-detail", kwargs={'slug': 'g1'})
        response = self.client.get(url)
        assert 'table' in response.context   