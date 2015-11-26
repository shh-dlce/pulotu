import os 
import sys

os.environ['DJANGO_SETTINGS_MODULE']='website.settings'
#os.environ['PYTHON_EGG_CACHE'] = '/srv/www/pulotu_website/.python-eggs/'

sys.path.append('/srv/www/pulotu_website')
sys.path.append('/srv/www/pulotu_website/website')
sys.path.append('/srv/www/pulotu_website/website/website')

sys.path.append('/usr/local/lib/python2.6/dist-packages/')
sys.path.append('/usr/local/lib/python2.7/dist-packages/')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()