from datetime import datetime
from django.db import models
from simple_history.models import HistoricalRecords


TYPES =(
    ('user','User'),
    ('workgroup','Workgroup')
)

STAT = (
    ('agent_present','AGENT_PRESENT'),
    ('agent_not_present','AGENT_NOT_PRESENT')
)

class QueuePrinciples(models.Model):
    principle_type = models.CharField(
        max_length=20,
        choices=TYPES,
        default='user',
    )
    principle_id = models.IntegerField(unique=True)
    display_name = models.CharField(
        max_length=200,
        default='',
        null= True,
        blank=True
    )
    online  = models.CharField(
        max_length=30,
        choices=STAT,
        default='agent_not_present',
    )
    last_active_at = models.DateTimeField(null=True,blank=True)
    last_assigned_at = models.DateTimeField(null=True,blank=True)
    principle_meta = models.JSONField(default=dict)
    history = HistoricalRecords()

    class Meta:
        db_table = "mevrik_queue_principles"


