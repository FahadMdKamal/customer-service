from django.db import models


class ContentTypeManager(models.Manager):
    pass


class ConverseContentType(models.Model):
    type_ref = models.CharField(max_length=100, unique=True)
    type_name = models.CharField(max_length=244)
    description = models.TextField(blank=True, null=True)
    content_icon = models.CharField(max_length=100, blank=True, null=True)
    config_keys = models.JSONField(blank=True, null=True)
    error_text_ref = models.CharField(max_length=244, blank=True, null=True)
    params = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ContentTypeManager()

    class Meta:
        db_table = 'converse_content_type'
