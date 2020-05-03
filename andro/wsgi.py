"""
WSGI config for andro project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(BASE_DIR, 'env/andro/lib/python3.7/site-packages'))

from django.core.wsgi import get_wsgi_application



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "andro.settings")

application = get_wsgi_application()
