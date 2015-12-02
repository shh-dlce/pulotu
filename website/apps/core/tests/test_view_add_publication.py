# coding: utf8
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from website.testutils import WithCompleteDatabase


class Test_View_PublicationForm(WithCompleteDatabase):
    def test_get_contact_form(self):
        self.login()
        response = self.client.get(reverse('AddPublication'))
        self.assertEqual(response.status_code, 200)

    def test_post_contact_form(self):
        self.login()
        response = self.client.post(
            reverse('AddPublication'),
            data={'link': 'n', 'reference': 'a@example.org'})
        self.assertEqual(response.status_code, 302)
