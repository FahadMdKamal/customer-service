from django.db import models

from .content import Content
from .custom_content_field import ContentCustomFields


FORMAT = (
    ('JSON', 'json'),
    ('BASE64', 'base64'),
    ('TEXT', 'text'),
    ('MARKDOWN', 'markdown'),
)


class ContentDataManager(models.Manager):
    pass


class ContentData(models.Model):
    field_id = models.ForeignKey(ContentCustomFields, null=True, blank=True, on_delete=models.PROTECT)
    content_id = models.ForeignKey(Content, null=True, blank=True, on_delete=models.PROTECT)
    field_key = models.CharField(max_length=244)
    field_value = models.CharField(max_length=100)
    value_format = models.CharField(max_length=100, choices=FORMAT, default='json')
    params = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ContentDataManager()

    class Meta:
        db_table = 'converse_content_data'
