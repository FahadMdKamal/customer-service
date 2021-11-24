from django.db import models

from mods.content.models.flow_node import FlowNode


class NodeConfigManager(models.Manager):
    pass


class NodeConfig(models.Model):
    flow_node = models.ForeignKey(FlowNode, on_delete=models.CASCADE, related_name='nodeconfigs')
    key = models.CharField(max_length=244)
    value = models.CharField(max_length=244)
    objects = NodeConfigManager()

    class Meta:
        db_table = 'content_node_config'