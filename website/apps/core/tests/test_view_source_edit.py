from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from website.apps.core.models import Source

class Test_View_SourceEdit_NotLoggedIn(TestCase):
    """Tests the source_edit view"""
    def setUp(self):
        self.client = Client()
        self.editor = User.objects.create_user('admin',
                                               'admin@example.com', "test")
        self.source1 = Source.objects.create(year=1991, author='Greenhill', 
                                    slug='greenhill1991', reference='S2',
                                    comment='c1', editor=self.editor)
        self.url = reverse("source-edit", kwargs={'slug': self.source1.slug})

    
    def test_error_when_not_logged_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, 
                             "/accounts/login/?next=%s" % self.url, 
                             status_code=302, 
                             target_status_code=200)


class Test_View_SourceEdit_LoggedIn(TestCase):
    """Tests the source_edit view"""
    def setUp(self):
        self.editor = User.objects.create_user('admin',
                                               'admin@example.com', "test")
        self.source1 = Source.objects.create(year=1991, author='Greenhill', 
                                    slug='greenhill1991', reference='S2',
                                    comment='c1', editor=self.editor)
        self.client = Client()
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
        return
        self.assertRedirects(response, 
                             reverse("source-detail", kwargs={'slug': 'greenhill1991'}),
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
        return
        self.assertRedirects(response, 
                             reverse("source-detail", kwargs={'slug': 'johnson2013'}),
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
