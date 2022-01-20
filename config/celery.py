from __future__ import absolute_import
import os
from django_mail_admin.models import Mailbox
from celery import Celery
from django.conf import settings
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


def fetch_mail():
    qs = Mailbox.objects.iterator()
    for mailbox in qs:
        mailbox.get_new_mail()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, fetch_mail(), name='add every 10')


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')