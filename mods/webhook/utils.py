import logging

from mods.webhook.models import Webhooks


logger = logging.getLogger('django')


class Webhook(object):
    def __init__(self, instance: Webhooks):
        self.instance = instance

    def dispatch_task(self):
        # TODO: Dispatch the task
        return

    def get_sender_kwargs(self, payload: dict) -> dict:
        kwargs = dict(target=self.instance.callback.get('url'),
                      timeout=self.instance.callback.get('timeout'),
                      payload=payload)
        return kwargs

    def delete(self) -> bool:
        self.instance.delete()
        return True
