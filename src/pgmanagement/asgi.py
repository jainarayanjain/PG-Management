"""
ASGI config for pgmanagement project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more panel on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pgmanagement.settings")

application = get_asgi_application()
