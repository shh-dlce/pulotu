from django.core.urlresolvers import reverse
from website.testutils import WithCompleteDatabase


class Test_CultureIndex(WithCompleteDatabase):
    def test_404_on_missing_culture(self):
        url = reverse("culture-detail", kwargs={'slug': 'fudge'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_find_valid_culture(self):
        url = reverse("culture-detail", kwargs={'slug': 'maori'})
        response = self.client.get(url)
        self.assertContains(response, 'Maori')
        url = reverse("culture-detail", kwargs={'slug': 'english'})
        response = self.client.get(url)
        self.assertContains(response, 'English')
    
    def test_has_responses(self):
        url = reverse("culture-detail", kwargs={'slug': 'maori'})
        response = self.client.get(url)
        #assert 'table' in response.context
