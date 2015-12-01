from django.conf import settings
from django.conf.urls import *
from django.views.generic import TemplateView, RedirectView
from django.contrib import admin
from django.conf.urls import patterns, include, url

from sitemap import sitemaps
from website.apps.core.views import RobotsTxt
from website.apps.survey.views import SurveyIndex

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Main Page / Home
    url(r'^select2/', include('django_select2.urls')),
    url(r'^$', 'website.apps.core.views.frontPage',
        name="index"),
    url(r'^faq', TemplateView.as_view(template_name="faq.html"), name="faq"),
    url(r'^dataset', TemplateView.as_view(template_name="dataset.html"), name="dataset"),
    url(r'^contactthanks', TemplateView.as_view(template_name="thankyou2.html"),
        name="thankyou2"),
    url(r'^captcha/', include('captcha.urls')),
    # About
    url(r'^about', 'website.apps.core.views.getPublications', name="about"),
    url(r'^AddPublication', 'website.apps.core.views.AddPublication',
        name="AddPublication"),
    url(r'^chooseexport', 'website.apps.survey.views.chooseexport', name="chooseexport"),
    url(r'^backend', TemplateView.as_view(template_name="backend.html"), name="backend"),
    url(r'^conditionsofuse', TemplateView.as_view(template_name="conditions.html"),
        name="conditionsofuse"),
    url(r'^refdownload', 'website.apps.survey.views.download_references',
        name="download_references"),
    url(r'^contact', 'website.apps.core.views.contact_form', name="contact"),
    url(r'^glossary', 'website.apps.core.views.glossary', name="glossary"),
    url(r'^logtest', 'website.apps.core.views.logUserIn', name="logtest"),
    url(r'^lockedout/$', TemplateView.as_view(template_name="lockouturl.html"),
        name="lockedout"),
    # url(r'^resetPW/$', 'website.apps.core.views.resetPW', name='resetPW'),

    # Core
    # ------------------------------------------------------------------------ #
    # Sitemap
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
    url(r'^search/', include("watson.urls", namespace="watson"),
        {'template_name': "search.html"}),
    # Robots.txt
    url(r'^robots\.txt$', RobotsTxt.as_view(), name='robots_txt'),

    # Sources
    url(r'^edit/source/add$', 'website.apps.core.views.SourceEdit', name="source-add"),
    url(r'^edit/source/(?P<slug>.+)$', 'website.apps.core.views.SourceEdit',
        name="source-edit"),

    # Cultures
    url(r'^culture/$', 'website.apps.core.views.CultureIndex', name="culture-index"),
    url(r'^culture/(?P<slug>.+)$', 'website.apps.core.views.details',
        name="culture-detail"),
    url(r'^edit/culture/add$', 'website.apps.core.views.CultureEdit', name="culture-add"),
    url(r'^edit/culture/(?P<slug>.+)$', 'website.apps.core.views.CultureEdit',
        name="culture-edit"),
    url(r'^compare/$', 'website.apps.core.views.compareCultures',
        name="compare_cultures"),

    # Survey
    url(r'^survey/$', SurveyIndex.as_view(),
        name="survey-index"),
    url(r'^survey/(?P<slug>.+)/$', 'website.apps.survey.views.indexx',
        name="survey-culture-index"),
    url(r'^survey/(?P<culture>.+)/(?P<section>.+)$',
        'website.apps.survey.views.SurveySectionEdit',
        name="survey-section-edit"),
    url(r'^stats/', include('website.apps.statistics.urls')),

    # ------------------------------------------------------------------------ #
    # Admin
    # ------------------------------------------------------------------------ #
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'},
        name="login"),
    url(r'^password_reset_complete/$', 'website.apps.core.views.PWreset',
        name="password_reset_complete"),
    url(r'^passwordreset/$', 'website.apps.core.views.resetPW', name="passwordreset"),
    url(r'^password_reset_done', 'django.contrib.auth.views.password_reset_done',
        name="password_reset_done"),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        name="password_reset_confirm"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name="logout"),
    url(r'^favicon\.ico$',
        RedirectView.as_view(url='%s/favicon.ico' % settings.STATIC_URL)),
)

# ------------------------------------------------------------------------ #
# Debug Media...
# ------------------------------------------------------------------------ #
if settings.DEBUG:  # pragma: no cover
    import debug_toolbar

    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
        # (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        # {'document_root': settings.MEDIA_ROOT}),
    )
