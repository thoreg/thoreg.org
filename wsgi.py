
import os
import sys

paths = [
    '/srv/w3/',
    '/srv/venvs/thoreg.org/lib/python2.6',
    '/srv/venvs/thoreg.org/lib/python2.6/site-packages/'
]
for path in paths:
    if path not in sys.path:
        sys.path.append(path)


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
settings_module = "%s.settings" % PROJECT_ROOT.split(os.sep)[-1]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
