import uuid as uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Webhooks(models.Model):
    class HookType(models.TextChoices):
        NOTIFY = 'notify', _('notify')
        CALLBACK = 'callback', _('callback')
        PUSH = 'push', _('push')
        RESPONSE = 'response', _('response')

    class Topic(models.TextChoices):
        MESSAGE = 'message', _('message')
        QUEUE = 'queue', _('queue')
        PROFILE = 'profile', _('profile')
        TAG = 'tag', _('tag')

    class Action(models.TextChoices):
        POST = 'post', _('post')
        DEL = 'del', _('del')
        REPLY = 'reply', _('reply')
        HISTORY = 'history', _('history')

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    app = models.CharField(max_length=45)
    type = models.CharField(max_length=10, choices=HookType.choices)
    topic = models.CharField(max_length=10, choices=Topic.choices)
    action = models.CharField(max_length=10, choices=Action.choices)
    summary = models.TextField()
    data = models.JSONField(default=dict)
    callback = models.JSONField(default=dict)
    target = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uuid
