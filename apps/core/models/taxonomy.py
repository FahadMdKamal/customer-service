from django.db import models
from django.utils.text import slugify


class TaxonomyManager(models.Manager):
    pass 


class Taxonomy(models.Model):
    taxonomy_type = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    details = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField()

    objects = TaxonomyManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            temp_slug = slugify((self.name, self.taxonomy_type))
            count = 0
            new_slug = temp_slug
            while Taxonomy.objects.filter(slug=new_slug).exists():
                count += 1
                new_slug = temp_slug + str(count)
            self.slug = new_slug
        return super().save(*args, **kwargs)
