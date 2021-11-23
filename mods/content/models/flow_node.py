from django.db import models

from mods.content.models import Flow


class FlowNodeManager(models.Manager):
    pass


class FlowNode(models.Model):
    name = models.CharField(max_length=244, null=True, blank=True) # To Create Blank Node
    flow = models.ForeignKey(Flow, on_delete=models.CASCADE)

    objects = FlowNodeManager()

    class Meta:
        db_table = 'content_flow_node'
