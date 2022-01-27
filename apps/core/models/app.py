# from django.db import models
# from django.contrib.auth.models import Group
# from django.utils.text import slugify


# class App(models.Model):
#     name = models.CharField(max_length=30)
#     slug = models.SlugField(unique=True)
#     groups = models.ManyToManyField(Group, related_name="app_groups")

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             slugified= slugify(self.name)
#             count = 0
#             new_slugified = slugified
#             while App.objects.filter(slug=new_slugified).exists():
#                 count += 1
#                 new_slugified = slugified + str(count)
#             self.slug = new_slugified
#         return super().save(*args, **kwargs)