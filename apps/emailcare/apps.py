from django.apps import AppConfig
from django.core.signals import request_started

class EmailcareConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.emailcare'
    from . import signals
    # request_finished.connect()
    # request_started.connect(signals)
