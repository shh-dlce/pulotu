# coding: utf8
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from mock import patch, Mock

from website.testutils import WithCompleteDatabase


class Test_View_ContactForm(WithCompleteDatabase):
    def test_get_contact_form(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_post_contact_form(self):
        mail = Mock()
        with patch('website.apps.core.views.mail', mail):
            response = self.client.post(
                reverse('contact'),
                data={'name': 'n',
                      'email': 'a@example.org',
                      'comment': 'c',
                      'captcha_0': 'passed',
                      'captcha_1': 'passed'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(mail.called)
