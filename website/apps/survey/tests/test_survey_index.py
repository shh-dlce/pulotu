from django.core.urlresolvers import reverse
from website.testutils import WithCompleteDatabase


class Test_View_SurveyIndex_NotLoggedIn(WithCompleteDatabase):
    def test_error_when_not_logged_in(self):
        response = self.client.get(reverse("survey-index"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            "/accounts/login/?next=%s" % reverse("survey-index"),
            status_code=302,
            target_status_code=200)

    def test_index(self):
        self.client.login(username="admin", password="test")
        response = self.client.get(reverse("survey-index"))
        self.assertContains(response, self.culture1.culture)
        self.assertContains(response, self.culture2.culture)
