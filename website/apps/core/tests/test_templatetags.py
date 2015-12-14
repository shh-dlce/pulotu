# coding: utf8
from __future__ import unicode_literals

from website.apps.core.models import Language
from website.testutils import WithEditor


class Tests(WithEditor):
    def setUp(self):
        WithEditor.setUp(self)
        self.language = self.object(Language, language='lname', isocode='abc')

    def test_language_map(self):
        from website.apps.core.templatetags.website_tags import language_map

        self.assertIn('abc', language_map(self.language))
        self.assertEquals(language_map(None), '')

    def test_links(self):
        from website.apps.core.templatetags import website_tags

        for name in ['ethnologue', 'glottolog', 'multitree', 'olac', 'llmap']:
            func = getattr(website_tags, 'link_' + name)
            self.assertIn('abc', func(self.language))
            self.assertEquals(func(None), '')
