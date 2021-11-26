import logging
from typing import Union

from mods.webhook.models import Webhooks
from mods.webhook.tasks import DeliverHook

logger = logging.getLogger('django')


class ReceiverWebhook(object):
    def __init__(self, instance: Union[Webhooks, None] = None):
        self.instance = instance

    def dispatch_task(self):
        # TODO: Dispatch the task
        return


class SenderWebhook(object):
    def __init__(self, hook_uid):
        self.hook_uid = hook_uid

    def send(self, payload: dict) -> bool:
        try:
            hook = Webhooks.objects.get(uuid=self.hook_uid)
            kwargs = dict(target=hook.callback.get('url'),
                          timeout=hook.callback.get('timeout'),
                          payload=payload)
            DeliverHook.apply_async(kwargs=kwargs)
            self.delete(hook)
            return True
        except Webhooks.DoesNotExist:
            logger.error('webhook objects does not exists')
            return False

    @staticmethod
    def delete(instance: Webhooks) -> bool:
        instance.delete()
        return True
