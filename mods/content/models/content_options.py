from django.db import models

from mods.content.models import Content


class ContentOptionsManager(models.Manager):
    pass


class ContentOptions(models.Model):
    content = models.ForeignKey(Content, null=True, blank=True, on_delete=models.PROTECT)
    option_name = models.CharField(max_length=255, blank=True, null=True)
    option_value = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ContentOptionsManager()

    class Meta:
        db_table = 'converse_content_options'