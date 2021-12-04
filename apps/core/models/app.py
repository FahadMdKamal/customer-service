from django.db import models
from django.contrib.auth.models import Group


class App(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    groups = models.ManyToManyField(Group, related_name="app_groups")

