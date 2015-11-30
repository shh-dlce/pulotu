from django.core.urlresolvers import reverse
from website.apps.core.models import Culture, Language
from website.testutils import WithEditor


class Test_View_CultureEdit_NotLoggedIn(WithEditor):
    """Tests the culture_edit view"""

    def setUp(self):
        WithEditor.setUp(self)
        culture1 = Culture.objects.create(
            culture='Maori',
            slug='maori',
            editor=self.editor)
        self.url = reverse("culture-edit", kwargs={'slug': culture1.slug})

    def test_error_when_not_logged_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            "/accounts/login/?next=%s" % self.url,
            status_code=302,
            target_status_code=200)


class Test_View_CultureEdit_LoggedIn(WithEditor):
    """Tests the culture_edit view"""

    def setUp(self):
        WithEditor.setUp(self)
        self.culture1 = Culture.objects.create(
            culture='Maori',
            slug='maori', editor=self.editor)
        self.lang = Language.objects.create(language='lname', id=1, editor=self.editor)
        self.client.login(username="admin", password="test")

    def test_404_on_missing_culture(self):
        response = self.client.get(reverse("culture-edit", kwargs={'slug': 'fudge'}))
        self.assertEqual(response.status_code, 404)

    def test_get_existing(self):
        response = self.client.get(
            reverse("culture-edit", kwargs={'slug': self.culture1.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Maori')

    def test_get_new(self):
        response = self.client.get(reverse("culture-add"))
        self.assertEqual(response.status_code, 200)

    def test_redirect_on_success(self):
        form_data = {
            'culture': "English",
            'notes': '',
            'submit': 'true',
            'languages': '1',
        }
        response = self.client.post(reverse("culture-add"), form_data)
        self.assertRedirects(
            response,
            reverse('survey-culture-index', kwargs={"slug": 'english'}),
            status_code=302,
            target_status_code=200)

    def test_slug_is_added(self):
        form_data = {
            'culture': "SOME CULTURE",
            'notes': '',
            'submit': 'true',
            'languages': '1',
        }
        response = self.client.post(reverse("culture-add"), form_data)
        self.assertRedirects(
            response,
            reverse('survey-culture-index', kwargs={"slug": 'some-culture'}),
            status_code=302,
            target_status_code=200)

    def test_error_on_duplicate_culture(self):
        form_data = {
            'culture': "Maori",
            'notes': '',
            'submit': 'true',
        }
        response = self.client.post(reverse("culture-add"), form_data)
        assert not response.context['form'].is_valid()
