from django.contrib.sites.models import Site
from django.conf import settings

def InjectSettings(context):
    """Injects various settings into the context"""
    site = Site.objects.get_current()
    authors = ", ".join([a[0] for a in settings.ADMINS])
    return {
        'SITE_AUTHORS': authors,
        'SITE_NAME': site.name,
        'SITE_DOMAIN': site.domain,
        'SITE_DESCRIPTION': getattr(settings, 'SITE_DESCRIPTION', ""),
    }
