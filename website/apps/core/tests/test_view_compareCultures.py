# coding: utf8
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from website.testutils import WithCompleteDatabase


class Test_View_SurveyIndex_NotLoggedIn(WithCompleteDatabase):
    def test_compare_cultures(self):
        response = self.client.get(reverse('compare_cultures'))
        self.assertEqual(response.status_code, 200)

    def test_compare_cultures_ajax(self):
        response = self.client.get(
            reverse('compare_cultures'),
            data={'question': 'where'},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
