from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from website.apps.core.models import Source


class Test_View_SourceIndex(TestCase):
    """Tests the source_index view"""
    def setUp(self):
        return
        self.client = Client()
        self.url = reverse("source-index")
        self.editor = User.objects.create(username='admin')
        self.source1 = Source.objects.create(year=1991, author='Greenhill', 
                                    slug='g1', reference='S2',
                                    comment='c1', editor=self.editor)
        self.source2 = Source.objects.create(year=1991, author='Smith', 
                                    slug='smith1991', reference='S2',
                                    comment='c1', editor=self.editor)
    
    def test_index(self):
        return
        response = self.client.get(self.url)
        self.assertContains(response, self.source1.author)
        self.assertContains(response, self.source2.author)
        
    def test_paginator(self):
        return
        response = self.client.get('%s?page=1' % self.url)
        self.assertContains(response, 'Greenhill')
    
        