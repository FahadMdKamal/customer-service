from django.db import models
from django.utils.text import slugify

class TexonomyManager(models.Manager):

    def get_texonomies_by_type(self, texonomy_type):
        print(texonomy_type)
    pass 


class Texonomy(models.Model):
    texonomy_type = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    details = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField()

    objects = TexonomyManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            temp_slug = slugify((self.name, self.texonomy_type))
            count = 0
            # print(Texonomy.objects.filter(slug=temp_slug).exists())
            while Texonomy.objects.filter(slug=temp_slug).exists():
                count += 1
                temp_slug = temp_slug + str(count)
            self.slug = temp_slug
        # return True
        # return self.objects.create(self, *args, **kwargs)
        return super(self, Texonomy).save(*args, **kwargs)
