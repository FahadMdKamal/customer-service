import requests

from celery import shared_task, Task
from celery.utils.log import get_task_logger
from config.celery import app

from mods.webhook.models import Webhooks
from mods.webhook.utils import ReceiverWebhook


logger = get_task_logger(__name__)


class DeliverHook(Task):
    max_retries = 5

    def run(self, target: str, timeout: int, payload: dict, **kwargs):
        timeout = timeout or 5
        try:
            response = requests.post(
                url=target,
                json=payload,
                headers={'Content-Type': 'application/json'},
                timeout=timeout
            )
            if response.status_code >= 500:
                response.raise_for_status()
        except requests.ConnectionError:
            delay_in_seconds = 2 ** self.request.retries
            self.retry(countdown=delay_in_seconds)


@shared_task
def process_webhook(hook_uid: str) -> bool:
    try:
        hook = Webhooks.objects.get(uuid=hook_uid)
        webhook = ReceiverWebhook(instance=hook)
        webhook.dispatch_task()
        return True
    except Webhooks.DoesNotExist:
        logger.error('webhook object not found')
        return False


DeliverHook = app.register_task(DeliverHook())
