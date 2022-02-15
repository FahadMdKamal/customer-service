from django.db import models
from django.utils.text import slugify
from django.db import models
import os, uuid, datetime

class FileManager:
    ''' Will manage files and photos '''
    @staticmethod
    def photo_path(instance, filename):

        basefilename, file_extension = os.path.splitext(filename)
        folder = file_extension.replace(".", "").upper()
        date = datetime.datetime.today()
        uid = uuid.uuid4()
        path = f'app-{instance.app_id}/{folder}/{uid}{file_extension}'
        return path


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
    
    # TODO: Change attachment field to File field and modify Serializer and views.
    # TODO: Start background process on resizing file to different formats and 
    # store those files url in the uploads log table.
    attachment = models.TextField(default=dict)

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
        return super(MessageTemplate, self).save(*args, **kwargs)
       