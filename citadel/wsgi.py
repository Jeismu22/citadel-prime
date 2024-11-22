"""
WSGI config for citadel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/munozjei2/munozjei2.pythonanywhere.com'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'nombre_de_tu_proyecto.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
