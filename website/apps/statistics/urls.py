from django.conf.urls import url, patterns

urlpatterns = patterns(
    '', url(r'^$', 'website.apps.statistics.views.statistics', name="statistics"))
