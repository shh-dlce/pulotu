from django.core.urlresolvers import reverse
from website.apps.core.models import Source
from website.testutils import WithEditor


class Test_View_SourceEdit_NotLoggedIn(WithEditor):
    """Tests the source_edit view"""

    def setUp(self):
        WithEditor.setUp(self)
        self.source1 = Source.objects.create(
            year=1991, author='Greenhill',
            slug='greenhill1991',
            reference='S2',
            comment='c1',
            editor=self.editor)
        self.url = reverse("source-edit", kwargs={'slug': self.source1.slug})

    def test_error_when_not_logged_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             "/accounts/login/?next=%s" % self.url,
                             status_code=302,
                             target_status_code=200)


class Test_View_SourceEdit_LoggedIn(WithEditor):
    """Tests the source_edit view"""

    def setUp(self):
        WithEditor.setUp(self)
        self.source1 = Source.objects.create(
            year=1991,
            author='Greenhill',
            slug='greenhill1991',
            reference='S2',
            comment='c1',
            editor=self.editor)
        self.client.login(username="admin", password="test")

    def test_404_on_missing_culture(self):
        response = self.client.get(
            reverse("source-edit", kwargs={'slug': 'fudge'})
        )
        self.assertEqual(response.status_code, 404)

    def test_get_existing(self):
        response = self.client.get(
            reverse("source-edit", kwargs={'slug': self.source1.slug})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Greenhill')

    def test_get_new(self):
        response = self.client.get(reverse("source-add"))
        self.assertEqual(response.status_code, 200)

    def test_redirect_on_success(self):
        form_data = {
            'year': 2013,
            'author': 'Johnson',
            'reference': '...',
            'submit': 'true',
        }
        response = self.client.post(reverse("source-add"), form_data)
        self.assertRedirects(
            response,
            reverse('admin:core_source_changelist'),
            status_code=302,
            target_status_code=200)

    def test_slug_is_added(self):
        form_data = {
            'year': 2013,
            'author': 'Johnson',
            'reference': '...',
            'submit': 'true',
        }
        response = self.client.post(reverse("source-add"), form_data)
        self.assertRedirects(
            response,
            reverse('admin:core_source_changelist'),
            status_code=302,
            target_status_code=200)

    def test_error_on_duplicate_culture(self):
        form_data = {
            'year': 1991,
            'author': 'Greenhill',
            'submit': 'true',
        }
        response = self.client.post(reverse("source-add"), form_data)
        assert not response.context['form'].is_valid()
