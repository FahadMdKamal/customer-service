from django.db import models

from .content_taxonomy import ContentTaxonomy

LANG = (
    ('BN', 'bn'),
    ('EN', 'en')
)


class ContentTextManager(models.Manager):
    pass


class ContentText(models.Model):
    text_ref = models.CharField(max_length=244) #TODO: Make it unique field, could be empty
    text_vars = models.JSONField(default=dict)
    text_body = models.JSONField(default=dict)
    text_group = models.ForeignKey(ContentTaxonomy, blank=True, null=True, on_delete=models.PROTECT)
    text_encoding = models.CharField(max_length=244, blank=True, null=True)
    template_type = models.CharField(max_length=244, blank=True, null=True)

    objects = ContentTextManager()

    class Meta:
        db_table = 'converse_content_text'
