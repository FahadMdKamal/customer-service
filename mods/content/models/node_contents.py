from django.db import models
from requests import delete

from . import Content
from .flow_node import FlowNode


class NodeContentManager(models.Manager):
    pass


class NodeContent(models.Model):
    flow_node = models.ForeignKey(FlowNode, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    objects = NodeContentManager()

    class Meta:
        db_table = 'content_node_contents'