from django.db import models
from django.utils.text import slugify


class Taxonomy(models.Model):
    app_id = models.CharField(max_length=255)
    taxonomy_type = models.CharField(max_length=50)
    context = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField()
    crumbs = models.CharField(max_length=255, null=True, blank=True)
    ref_path = models.CharField(max_length=255, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    display_order = models.IntegerField(default=0)
    photo_url = models.URLField(null=True, blank=True)
    details = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'core_taxonomy'
        unique_together = ('taxonomy_type', 'name')

    def save(self, *args, **kwargs):
        if not self.slug:
            temp_slug = slugify(self.name)
            count = 0
            new_slug = temp_slug
            while Taxonomy.objects.filter(slug=new_slug).exists():
                count += 1
                new_slug = temp_slug + str(count)
            self.slug = new_slug
        return super().save(*args, **kwargs)
