from django.db import models
from .content_taxonomy import ContentTaxonomy


class FlowManager(models.Manager):
    pass


class Flow(models.Model):
    name = models.CharField(max_length=244)
    app_id = models.CharField(max_length=244, blank=True, null=True)
    group = models.ForeignKey(ContentTaxonomy, blank=True, null=True)
    objects = FlowManager()

    class Meta:
        db_table = 'converse_content_data'