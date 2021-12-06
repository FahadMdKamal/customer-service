from django.db import models
from django.utils.text import slugify

import chevron


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

    def save(self, *args, **kwargs):
        if not self.template_code:
            temp_code= slugify(self.name)
            count = 0
            new_template_code = temp_code
            while MessageTemplate.objects.filter(template_code=new_template_code).exists():
                count += 1
                new_template_code = temp_code + str(count)
            self.template_code = new_template_code
        return super().save(*args, **kwargs)

    def prepare_template(self):
        tvs = self.template_vars[0]
        for t in tvs.items():
            print(t)

        # value = eval('value_resolver()')
        # if not value:
        #     value = value['default']
        # return value


# from mods.content.models import MessageTemplate
# mt = MessageTemplate.objects.all().first()
# mt.prepare_template()

# [{"key": "today", "default": "jani na", "value_resolver": "func_date_today"}]