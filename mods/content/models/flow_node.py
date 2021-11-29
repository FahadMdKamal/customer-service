from django.db import models

from mods.content.models import Flow


class FlowNodeManager(models.Manager):
    pass


class FlowNode(models.Model):
    name = models.CharField(max_length=244, null=True, blank=True)  # To Create Blank Node
    flow = models.ForeignKey(Flow, on_delete=models.CASCADE, related_name='flownodes')
    node_type = models.CharField(max_length=255, null=True, blank=True)

    objects = FlowNodeManager()

    class Meta:
        db_table = 'content_flow_node'
