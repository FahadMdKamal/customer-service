from django.db import models
from .case_id import CaseId


class CaseMessage(models.Model):

    MESSAGE_TYPE = (
            ('comment', 'Comment'),
            ('voice', 'Voice'),
            ('message', 'Message'),
            ('email', 'Email'),
        )

    BODY_FORMAT = (
            ('plain', 'Plain'),
            ('html', 'Html'),
            ('markdown', 'Markdown'),
        )

    caseid = models.ForeignKey(CaseId, on_delete=models.CASCADE, related_name="case_message")
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, related_name='case_message_parent', null=True, blank=True)
    from_aud_id = models.IntegerField(default=0)
    to_aud_id = models.IntegerField(default=0)
    message_type = models.CharField(
        max_length=20,
        choices=MESSAGE_TYPE,
        default='message',
    )
    platform = models.CharField(max_length=100,null=True, blank=True)
    source_ref = models.IntegerField(default=0)
    body = models.TextField(null=True, blank=True)
    plain_body = models.TextField(null=True, blank=True)
    body_format = models.CharField(
        max_length=20,
        choices=BODY_FORMAT,
        default='plain',
    )
    metadata = models.JSONField(default=dict, null= True, blank=True)
    attachments = models.JSONField(default=dict, null=True, blank=True)
    via = models.JSONField(default=dict, null= True, blank=True)
    public= models.CharField(max_length=50, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "casex_case_message"
        