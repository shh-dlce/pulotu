import autocomplete_light

from website.apps.core.models import Source

autocomplete_light.register(
    Source,
    search_fields=['author'],
    autocomplete_js_attributes={'placeholder': 'Response'})
