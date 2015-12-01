from django.contrib.sitemaps import Sitemap
from website.apps.core.models import Culture


class CultureSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return Culture.objects.all().order_by("-added")

    def lastmod(self, obj):
        return obj.added


sitemaps = {
    'cultures': CultureSitemap,
}
