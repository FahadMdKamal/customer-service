from django.db import models


class MessageTemplate(models.Model):
    app_id = models.IntegerField(default=0)
    name = models.CharField(max_length=244)
    template_code = models.CharField(max_length=244, unique=True)
    template_type = models.CharField(
        max_length=15,
        choices=(
            ('message', 'Message'),
            ('email', 'Email')
        ),
        default='message',
    )
    template_format = models.CharField(
        max_length=15,
        choices=(
            ('text', 'Text'),
            ('markdown', 'Markdown'),
            ('mustache', 'Mustache'),
        ),
        default='text',
    )
    body_template = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    template_vars = models.JSONField(default=dict, blank=True, null=True)
    value_resolver = models.CharField(max_length=255, null=True, blank=True)
    app_id = models.IntegerField(default=0)
    template_group_id = models.IntegerField(default=1, null=True, blank=True)

    allowed_channel_types = models.JSONField(default=dict, blank=True, null=True)
    attachments = models.JSONField(default=dict, blank=True, null=True)
    status = models.CharField(
        max_length=15,
        choices=(
            ('active', 'Active'),
            ('inactive', 'In Active'),
            ('draft', 'Draft'),
        ),
        default='active',
    )
    usage_count = models.CharField(max_length=255, null=True, blank=True)
    owner = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'content_message_template'
   