from django.contrib.auth.models import User
from django.test import TestCase
from website.apps.core.models import Source


class Test_Source(TestCase):
    """Tests the Source Model"""
    def setUp(self):
        self.editor = User.objects.create(username='admin')

    def test_repr(self):
        """Test source's special handling of repr"""
        s = Source.objects.create(
            year=1991,
            author='Smith',
            slug='Smith1991',
            reference='S2',
            comment='c1',
            editor=self.editor)
        self.assertEquals(s.__unicode__(), "%s (%d)" % (s.author, s.year))
        s.year = None
        self.assertEquals(s.__unicode__(), s.author)
