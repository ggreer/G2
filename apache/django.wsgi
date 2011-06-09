import os
import sys
sys.path.extend(['/home/ggreer', '/home/ggreer/pydj', '/home/ggreer/pydj/apps'])

os.environ['DJANGO_SETTINGS_MODULE'] = 'pydj.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
