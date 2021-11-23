from django.db import models
from .content_taxonomy import ContentTaxonomy


class NodeContentManager(models.Manager):
    pass


class NodeContent(models.Model):
    flow_node = models.ForeignKey()
    content = models.ForeignKey()
    objects = NodeContentManager()

    class Meta:
        db_table = 'content_node_contents'