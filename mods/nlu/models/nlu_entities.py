from enum import unique

from django.db import models


class NluEntities(models.Model):
    name = models.CharField(max_length=244, unique=True)
    role = models.CharField(max_length=244, null=True, blank=True)
    confidence_score = models.IntegerField(null=True, blank=True)
    value = models.CharField(max_length=244, null=True, blank=True)
    position = models.JSONField(null=True, blank=True)
    value_parser = models.CharField(max_length=244, null=True, blank=True)
    value_config = models.CharField(max_length=244, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'nlu_entities'

    def __str__(self):
        return self.name
