from django.db import models

from .content_text import ContentText


class ContentVarsManager(models.Manager):
    pass


class ContentVars(models.Model):
    var_type = models.CharField(max_length=100)
    var_key = models.CharField(max_length=244)
    var_mapping = models.CharField(max_length=244)
    default_value = models.CharField(max_length=100)
    optional = models.CharField(max_length=244)
    content_text = models.ForeignKey(ContentText, blank=True, null=True, on_delete=models.PROTECT)
    params = models.JSONField()

    objects = ContentVarsManager()

    class Meta:
        db_table = 'converse_content_vars'
