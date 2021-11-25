from django.db import models
from django.utils.text import slugify

class TexonomyManager(models.Manager):

    def get_texonomies_by_type(self, texo_name):
        pass
    pass 


class Texonomy(models.Model):
    texonomy_type = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    details = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField()

    objects = TexonomyManager()

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify((self.name,self.texonomy_type))
        return super().save(*args, **kwargs)
