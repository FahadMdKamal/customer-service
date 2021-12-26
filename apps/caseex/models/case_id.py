from django.db import models
from uuid import uuid4
import datetime

class CaseId(models.Model):
    app_id = models.IntegerField(default=0)
    source_ref = models.IntegerField(default=0)
    ref_id = models.CharField(max_length=100, help_text="auto generated with app_id,date,shot_uuid", null=True, blank=True)
    subject = models.CharField(max_length=100)
    description = models.TextField(),
    external_id = models.IntegerField(default=0),
    group_id = models.IntegerField(default=0)
    metadata= models.JSONField(default=dict, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=(
            ('new', 'New'),
            ('open', 'Open'),
            ('hold', 'Hold'),
            ('closed', 'Closed'),
            ('escalated', 'Escalated'),
        ),
        default='new',
    )
    options = models.CharField(
        max_length=50,
        choices=(
            ('allow_attachments', 'Allow Attachments'),
            ('allow_threaded_replies', 'Allow Threaded Replies'),
            ('closed_replay', 'Closed Replay'),
        ),
        default='allow_attachments',
    )
    case_tags = models.CharField(max_length=20,null=True, blank=True)
    case_priority = models.CharField(
        max_length=20,
        choices=(
            ('low', 'Low'),
            ('normal', 'Normal'),
            ('high', 'High'),
        ),
        default='low',
    )
    case_type = models.CharField(
        max_length=20,
        choices=(
            ('support', 'Support'),
            ('problem', 'Problem'),
            ('incident', 'Incident'),
            ('question', 'Question'),
            ('task', 'Task'),
        ),
        default='support',
    )
    case_url = models.URLField(null= True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "caseex_CaseId"

    def save(self):
        if not self.ref_id:
            self.ref_id = f"{self.app_id}-{str(uuid4())[:8]}-{datetime.datetime.today().date()}"
        super().save()