from django.db import models

from apps.core.models import Taxonomy


class FlowManager(models.Manager):
    pass


class Flow(models.Model):
    name = models.CharField(max_length=244, null=True, blank=True)
    app_id = models.CharField(max_length=244, blank=True, null=True)
    group = models.ForeignKey(Taxonomy, blank=True, null=True, on_delete=models.CASCADE)
    objects = FlowManager()

    class Meta:
        db_table = 'content_flow'
