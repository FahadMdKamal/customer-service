from datetime import datetime, timedelta, timezone
from celery import shared_task
from django.core.serializers import serialize
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def set_escalated_status(data):
    from mods.queue_service.models.queue_items import QueueItems
    pk = data.get('pk')
    try:
        queue_object = QueueItems.objects.get(pk=pk)
    except:
        print(f"Failed retrieving order object of id {pk}")
        return

    queue_object.status = 'unattended' 
    queue_object.save(update_fields=['status', ]) 
    return True

@shared_task
def set_dispute_status(data):
    from mods.queue_service.models.queue_items import QueueItems
    pk = data.get('pk')
    try:
        queue_object = QueueItems.objects.get(pk=pk)
    except:
        print(f"Failed retrieving order object of id {pk}")
        return

    queue_object.status = 'disputed' 
    queue_object.save(update_fields=['status', ]) 
    return True
  

    