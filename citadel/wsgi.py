"""
WSGI config for citadel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""


import os
import sys

# Añadir el directorio de tu proyecto al path
project_home = '/home/munozjei2/citadel-prime'  # Ruta donde está tu proyecto
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Establecer el entorno virtual
activate_this = '/home/munozjei2/citadel-prime/myenv/bin/activate_this.py'
exec(open(activate_this).read(), {'__file__': activate_this})

# Configurar Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'  # Ajusta esto a tu archivo settings.py
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
