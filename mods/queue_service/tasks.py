from datetime import datetime, timedelta, timezone
from celery import shared_task
from celery.schedules import crontab
from django.core.serializers import serialize
from celery.utils.log import get_task_logger
from django.db.models import Q
from mevrik.celery import app
from mevrik.celery import task

logger = get_task_logger(__name__)

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Call every 2 hours 52 min.
    sender.add_periodic_task(
        30.0,
        set_updated_status.s()
    )
    # sender.add_periodic_task(crontab(), test.s('hello'), name='add every 10')



@task
def set_updated_status():
    from mods.queue_service.models.queue_items import QueueItems
    data = QueueItems.objects.filter(Q(status="pending")|Q(status="attended")|Q(status="unattended"))
    for n in data:
        t =(datetime.now() - n.updated_at).total_seconds()
        print(t)
        if int(t) > int(n.escalation_timeout) and n.status=='attended':
            QueueItems.objects.filter(id=n.id).update(status="unattended")
        if int(t) > int(n.dispute_timeout):
            QueueItems.objects.filter(id=n.id).update(status="disputed")

    return True

  

    