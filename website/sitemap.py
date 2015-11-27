from django.contrib.sitemaps import Sitemap
from website.apps.core.models import Culture, Language, Source


class LanguageSitemap(Sitemap):
    changefreq = "never"
    priority = 0.1
    
    def items(self):
        return Language.objects.all().order_by("-added")

    def lastmod(self, obj):
        return obj.added


class CultureSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0
    
    def items(self):
        return Culture.objects.all().order_by("-added")

    def lastmod(self, obj):
        return obj.added


class SourceSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
    
    def items(self):
        return Source.objects.all().order_by("-added")

    def lastmod(self, obj):
        return obj.added


sitemaps = {
    # 'languages': LanguageSitemap,
    'sources': SourceSitemap,
    'cultures': CultureSitemap,
}
