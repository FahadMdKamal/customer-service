
from datetime import datetime, timedelta, timezone
from django.db import models
from django.core.serializers import serialize
from simple_history.models import HistoricalRecords



TOPICS=(
    ('social','Social'),
    ('email','Email'),
    ('live_chat','Live_Chat'),
    ('live_call','Live_Call'),
    ('support','Support')
)

STATUS = (
    ('incative','Inactive'),
    ('attended','Attended'),
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
        max_length=20,
    )
    source_ref = models.CharField(
        max_length=200,
        default='',
        null= True,
        blank=True
    )
    principle_id = models.IntegerField()
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
    escalation_timeout = models.IntegerField(default=0)
    dispute_timeout = models.IntegerField(default=0)
    history = HistoricalRecords()

    class Meta:
        db_table = "mevrik_queue_items"

    def save(self,*args, **kwargs):
        # create_task = False # variable to know if celery task is to be created
        # if self.id is None: # Check if instance has 'pk' attribute set 
        #     # Celery Task is to created in case of 'INSERT'
        #     create_task = True # set the variable 
        super(QueueItems, self).save(*args, **kwargs)
        
        from mods.queue_service.tasks import set_escalated_status,set_dispute_status

        if self.status== 'attended':
            escalated_time = datetime.fromtimestamp((self.updated_at).timestamp(), tz=timezone.utc) + timedelta(seconds=int(self.escalation_timeout))
            # expire =datetime.fromtimestamp((self.updated_at).timestamp(), tz=timezone.utc) + timedelta(seconds=int(self.escalation_timeout)+1)
            set_escalated_status.apply_async(args=[{'pk':self.id}], eta=escalated_time,expires=5)
        print('aekak')
        dispute_time = datetime.fromtimestamp((self.updated_at).timestamp(), tz=timezone.utc) + timedelta(seconds=int(self.dispute_timeout))
        set_dispute_status.apply_async(args=[{'pk':self.id}], eta=dispute_time,expires=5)
        
 
        
            


