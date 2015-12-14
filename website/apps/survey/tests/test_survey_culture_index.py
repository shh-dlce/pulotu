from django.core.urlresolvers import reverse

from website.testutils import WithCompleteDatabase


class Tests(WithCompleteDatabase):
    """Tests the survey_index view"""
    def test_error_when_not_logged_in(self):
        url = reverse("survey-culture-index", kwargs={'slug': 'english'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             "/accounts/login/?next=%s" % url,
                             status_code=302,
                             target_status_code=200)

    def test_404_on_missing_culture(self):
        self.client.login(username="admin", password="test")
        response = self.client.get(
            reverse("survey-culture-index", kwargs={'slug': 'fudge'}))
        self.assertEqual(response.status_code, 404)

    def test_context(self):
        self.client.login(username="admin", password="test")
        response = self.client.get(
            reverse("survey-culture-index", kwargs={'slug': 'english'}))
        assert 'full' in response.context

    def test_page(self):
        self.client.login(username="admin", password="test")
        response = self.client.get(
            reverse("survey-culture-index", kwargs={'slug': 'maori'}))
        self.assertContains(response, self.culture1.culture)
