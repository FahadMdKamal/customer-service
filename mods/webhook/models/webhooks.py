import uuid as uuid
from django.db import models


class Webhooks(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    app = models.CharField(max_length=45)
    topic = models.CharField(max_length=8)
    action = models.CharField(max_length=8)
    summary = models.TextField()
    data = models.JSONField(default=dict)
    callback = models.JSONField(default=dict)
    target = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uuid
