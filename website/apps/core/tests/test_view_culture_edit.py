from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from website.apps.core.models import Culture

class Test_View_CultureEdit_NotLoggedIn(TestCase):
    """Tests the culture_edit view"""
    def setUp(self):
        self.client = Client()
        self.editor = User.objects.create_user('admin',
                                               'admin@example.com', "test")
        self.culture1 = Culture.objects.create(culture='Maori', 
                                    slug='maori',editor=self.editor)
        self.url = reverse("culture-edit", kwargs={'slug': self.culture1.slug})

    
    def test_error_when_not_logged_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, 
                             "/accounts/login/?next=%s" % self.url, 
                             status_code=302, 
                             target_status_code=200)


class Test_View_CultureEdit_LoggedIn(TestCase):
    """Tests the culture_edit view"""
    def setUp(self):
        self.editor = User.objects.create_user('admin',
                                               'admin@example.com', "test")
        self.culture1 = Culture.objects.create(culture='Maori', 
                                    slug='maori',editor=self.editor)
        self.client = Client()
        self.client.login(username="admin", password="test")

    def test_404_on_missing_culture(self):
        response = self.client.get(
            reverse("culture-edit", kwargs={'slug': 'fudge'})
        )
        self.assertEqual(response.status_code, 404)

    def test_get_existing(self):
        response = self.client.get(
            reverse("culture-edit", kwargs={'slug': self.culture1.slug})
        )
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
        }
        response = self.client.post(reverse("culture-add"), form_data)
        self.assertRedirects(response, 
                             reverse("culture-detail", kwargs={'slug': 'english'}),
                             status_code=302, 
                             target_status_code=200)

    def test_slug_is_added(self):
        form_data = {
            'culture': "SOME CULTURE",
            'notes': '',
            'submit': 'true',
        }
        response = self.client.post(reverse("culture-add"), form_data)
        self.assertRedirects(response, 
                             reverse("culture-detail", kwargs={'slug': 'some-culture'}),
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
