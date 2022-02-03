from django.db import models
from uuid import uuid4
import datetime
from django.utils.text import slugify


class CaseId(models.Model):
    STATUS = (
        ('new', 'New'), ('open', 'Open'), ('hold', 'Hold'),
        ('closed', 'Closed'), ('escalated', 'Escalated')
    )
    OPTIONS = (
        ('allow_attachments', 'Allow Attachments'),
        ('allow_threaded_replies', 'Allow Threaded Replies'),
        ('closed_replay', 'Closed Replay'),
    )
    CASE_PRIORITY = (('low', 'Low'), ('normal', 'Normal'), ('high', 'High'))
    CASE_TYPE = (
        ('support', 'Support'),
        ('problem', 'Problem'),
        ('incident', 'Incident'),
        ('question', 'Question'),
        ('task', 'Task'),
    )

    app_id = models.IntegerField(default=0)
    source_ref = models.IntegerField(default=0)
    ref_id = models.CharField(max_length=100, help_text="auto generated with app_id,date,shot_uuid", null=True,
                              blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(),
    external_id = models.IntegerField(default=0),
    group_id = models.IntegerField(default=0)
    metadata = models.JSONField(default=dict, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='new',
    )
    options = models.CharField(
        max_length=50,
        choices=OPTIONS,
        default='allow_attachments',
    )
    case_tags = models.CharField(max_length=20, null=True, blank=True)
    case_priority = models.CharField(
        max_length=20,
        choices=CASE_PRIORITY,
        default='low',
    )
    case_type = models.CharField(
        max_length=20,
        choices=CASE_TYPE,
        default='support',
    )
    case_url = models.SlugField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "casex_case_id"

    def save(self):
        if not self.ref_id:
            self.ref_id = f"{self.app_id}-{str(uuid4())[:8]}-{datetime.datetime.today().date()}"

        if not self.case_url:
            temp_slug = slugify(self.ref_id)
            count = 0
            new_slug = temp_slug
            while CaseId.objects.filter(case_url=new_slug).exists():
                count += 1
                new_slug = temp_slug + "-" + str(count)
            self.case_url = new_slug
        super().save()
