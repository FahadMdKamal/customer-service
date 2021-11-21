from django.db import models
from .static_dictionary import StaticDictionary

MARKED = (
    ('Favourite', 'Favourite'),
    ('Like', 'Like'),
)


class NluIntent(models.Model):
    name = models.CharField(max_length=244, unique=True)
    short_code = models.CharField(max_length=244, unique=True)
    group = models.ForeignKey(StaticDictionary, on_delete=models.CASCADE, null=True, blank=True)
    marked = models.CharField(choices=MARKED, max_length=50, default='Favourite')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'nlu_intent'

    def __str__(self):
        return self.name
