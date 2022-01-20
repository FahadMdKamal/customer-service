
from django.db import models

TOPICS=(
    ('social','Social'),
    ('email','Email'),
    ('live_chat','Live_Chat'),
    ('live_call','Live_Call'),
    ('support','Support')
)

STATUS = (
    ('incative','Inactive'),
    ('pending','Pending'),
    ('closed','Closed'),
    ('unattended','Unattended'),
    ('disputed','Disputed')
)

class QueueItems(models.Model):
    app_id = models.IntegerField()
    topic = models.SlugField(
        max_length=40,
        choices= TOPICS,
        default='social',
    )
    serial = models.CharField(
        max_length=20
    )
    source_ref = models.CharField(
        max_length=200,
        default='',
        null= True,
        blank=True
    )
    principle_id = models.IntegerField(default=0)
    queue_variant = models.CharField(
        max_length=200,
        default='',
        null= True,
        blank=True
    )
    item_subject = models.CharField(
        max_length=200,
        default='',
        null= True,
        blank=True
    )
    item_from_ref = models.CharField(
        max_length=100,
        default='',
        null= True,
        blank=True
    )
    item_to_ref = models.CharField(
        max_length=100,
        default='',
        null= True,
        blank=True
    )
    priority = models.CharField(
        max_length=100,
        default='normal',
    )
    status = models.CharField(
        max_length=100,
        choices= STATUS,
        default= 'pending'
    )
    metadata = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "mevrik_queue_items"


