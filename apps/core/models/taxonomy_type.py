from django.db import models


class TaxonomyType(models.Model):
    context = models.CharField(max_length=255, null=True, blank=True)
    app_id = models.CharField(max_length=255, null=True, blank=True)
    taxonomy_type = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    parent_type = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    details = models.CharField(
        max_length=20,
        choices=(
            ('DESCRIPTION', 'Description'),
            ('PLURAL', 'plural'),
        ),
        default='DESCRIPTION',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'core_taxonomy_type'
