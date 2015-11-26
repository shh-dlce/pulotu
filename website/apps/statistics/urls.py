from django.conf.urls import *

urlpatterns = patterns('',
    url(r'^$', 
        'website.apps.statistics.views.statistics', 
        name="statistics"
    ),
)
