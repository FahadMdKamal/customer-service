from django.db import models
from apps.core.models import Taxonomy


class MessageTemplateManager(models.Manager):
    pass


class MessageTemplate(models.Model):
    template_code = models.CharField(max_length=244, unique=True)
    template_type = models.CharField(
        max_length=15,
        choices=(
            ('message', 'message'),
            ('email', 'email')
        ),
        default='',
    )
    template_format = models.CharField(
        max_length=15,
        choices=(
            ('text', 'text'),
            ('markdown', 'markdown')
        ),
        default='',
    )
    body_template = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    template_var = models.TextField(null=True, blank=True)
    value_resolver = models.CharField(max_length=255, null=True, blank=True)
    app_id = models.IntegerField(default=0)
    template_group = models.ForeignKey(Taxonomy, on_delete=models.CASCADE, null=True, blank=True)

    allowed_channel_types = models.CharField(
        max_length=15,
        choices=(
            ('live-chat', 'Live Chat'),
            ('messenger', 'Messenger'),
            ('comment', 'Comment'),
        ),
        default='',
    )
    attachment = models.CharField(max_length=15, null=True, blank=True)
    status = models.CharField(
        max_length=15,
        choices=(
            ('active', 'Active'),
            ('inactive', 'In Active'),
            ('draft', 'Draft'),
        ),
        default='',
    )
    usage_count = models.CharField(max_length=255, null=True, blank=True)
    owner = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MessageTemplateManager()

    class Meta:
        db_table = 'content_message_template'
