# Django settings for website project.
import os

SITE_ROOT = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
AXES_USE_USER_AGENT = True
AXES_LOCKOUT_TEMPLATE = 'lockouturl.html'
AXES_LOCKOUT_URL = 'lockedout'
AXES_LOGIN_FAILRE_LIMIT = 2
DEBUG = TEMPLATE_DEBUG = False
ENABLE_SELECT2_MULTI_PROCESS_SUPPORT = True

ADMINS = (
)

INTERNAL_IPS = ('127.0.0.1',)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'TEST_NAME': None,
    }
}

# Site details
SITE_NAME = 'Pulotu'
SITE_ID = 1
SITE_DOMAIN = 'localhost'
SITE_DESCRIPTION = "Pacific Religion Database"

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = "/"

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.abspath(os.path.join(os.path.split(SITE_ROOT)[0], 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '../static_root/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(os.path.split(SITE_ROOT)[0], 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.eggs.Loader'
    )),
)

MIDDLEWARE_CLASSES = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'djangosecure.middleware.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'axes.middleware.FailedLoginMiddleware',
]

ROOT_URLCONF = 'website.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'website.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "website.apps.core.context_processors.InjectSettings",
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django.contrib.redirects',
    # Admin site
    'django.contrib.admin',
    'django.contrib.admindocs',

    # third-party
    'south',  # south: database migrations
    'reversion',  # reversion: object version control.
    'djangosecure',  # django-secure: Security helper
    'django_tables2',  # django-tables2: tables helper
    'watson',  # search
    'compressor',  # django-compressor for asset compression
    'captcha',
    'django_select2',
    'axes',
    # website
    'website.apps.core',  # core functionality
    'website.apps.survey',  # survey
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format':
                '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'file_logging': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'backupCount': 0,
            'maxBytes': 5000000,
            'filename': 'django.log',
            'filters': ['require_debug_false'],
        },
        'db_logging': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'backupCount': 0,
            'maxBytes': 5000000,
            'filename': 'django-db.log',
            'filters': ['require_debug_false'],
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
    },

    'loggers': {
        'django': {
            'handlers': ['file_logging'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db': {
            'handlers': ['db_logging'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django_select2': {
            'handlers': ['db_logging'],
            'level': 'DEBUG',
            'propogate': True,
        },
    }
}

# Caching:
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache',
        'KEY_PREFIX': SITE_NAME,
    }
}
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

# maximum age of persistent database connection
CONN_MAX_AGE = 64

# THIRD-PARTY SETTINGS ==========================================

# Django-Security settings
SECURE_FRAME_DENY = True  # prevent framing of pages.
SECURE_BROWSER_XSS_FILTER = True  # enable XSS protection
SESSION_COOKIE_SECURE = False  # can't login with True?
SESSION_COOKIE_HTTPONLY = False  # can't login with True?
SECURE_CONTENT_TYPE_NOSNIFF = True

# South
SOUTH_TESTS_MIGRATE = False  # just use syncdb

# Static Sitemaps
STATICSITEMAPS_ROOT_SITEMAP = 'website.sitemap.sitemap'
