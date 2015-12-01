# coding: utf8
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from website.testutils import WithCompleteDatabase


class Tests(WithCompleteDatabase):
    def test_glossary(self):
        response = self.client.get(reverse('glossary'))
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_sitemap(self):
        response = self.client.get('/sitemap.xml')
        self.assertEqual(response.status_code, 200)
