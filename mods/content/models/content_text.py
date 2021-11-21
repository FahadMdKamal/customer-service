from django.db import models

from .content_taxonomy import ContentTaxonomy

LANG = (
    ('BN', 'bn'),
    ('EN', 'en')
)


class ContentTextManager(models.Manager):
    pass


class ContentText(models.Model):
    text_ref = models.CharField(max_length=244)
    parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT)
    lang = models.CharField(max_length=244, choices=LANG)
    text_body = models.TextField()
    has_vars = models.BooleanField()
    error_text_ref = models.CharField(max_length=244)
    text_group = models.ForeignKey(ContentTaxonomy, blank=True, null=True, on_delete=models.PROTECT)
    text_encoding = models.CharField(max_length=244)
    template_type = models.CharField(max_length=244)

    objects = ContentTextManager()

    class Meta:
        db_table = 'converse_content_text'
