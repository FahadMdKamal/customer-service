from django.db import models

from mods.content.models import Flow, Content

NODE_TYPE = (
    ('Start', 'start'),
    ('Content', 'content'),
)

class FlowNodeManager(models.Manager):
    pass


class FlowNode(models.Model):
    name = models.CharField(max_length=244, null=True, blank=True)  # To Create Blank Node
    flow = models.ForeignKey(Flow, on_delete=models.CASCADE, related_name='flownodes')
    node_type = models.CharField(max_length=255, null=True, blank=True, choices=NODE_TYPE)
    content_type = models.CharField(max_length=255, null=True, blank=True)
    initial_content_id = models.ForeignKey(Content, on_delete=models.CASCADE, blank=True, null=True)

    objects = FlowNodeManager()

    class Meta:
        db_table = 'content_flow_node'
