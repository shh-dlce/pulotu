# coding: utf8
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from website.testutils import WithCompleteDatabase


class Test_View_SurveyIndex_NotLoggedIn(WithCompleteDatabase):
    def test_download_dataset(self):
        self.client.login(username="admin", password="test")

        response = self.client.post(reverse('chooseexport'))
        self.assertEqual(response.status_code, 400)

        response = self.client.get(reverse('chooseexport'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('chooseexport'), data=dict(questions='1'))
        self.assertEqual(response.status_code, 200)

    def test_download_references(self):
        self.client.login(username="admin", password="test")

        response = self.client.post(reverse('download_references'))
        self.assertEqual(response.status_code, 200)
        self.client.post(reverse('download_references'))
