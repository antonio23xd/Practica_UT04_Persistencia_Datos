"""
ASGI config for Practica_UT04_Persistencia_Datos project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Practica_UT04_Persistencia_Datos.settings')

application = get_asgi_application()
