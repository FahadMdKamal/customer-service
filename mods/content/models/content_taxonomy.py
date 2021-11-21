from django.db import models

TAXONOMY_TYPE = (
    ('TEXT_GROUP', 'text_group'),
    ('CATEGORY', 'category'),
    ('ACTION', 'action'),
)


class ContentTaxonomyManager(models.Manager):
    pass


class ContentTaxonomy(models.Model):
    taxonomy_type = models.CharField(max_length=100, choices=TAXONOMY_TYPE)
    name = models.CharField(max_length=244)
    taxonomy_slug = models.SlugField(max_length=244)
    description = models.TextField()
    parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT)
    display_order = models.CharField(max_length=244)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ContentTaxonomyManager()

    class Meta:
        db_table = 'converse_content_taxonomy'
