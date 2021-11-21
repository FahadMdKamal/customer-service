from enum import unique

from django.db import models
from .nlu_intent import NluIntent


class NluUtterances(models.Model):
    name = models.CharField(max_length=244)
    intent = models.ForeignKey(NluIntent, on_delete=models.CASCADE)
    intent_confidence = models.FloatField(default=0.00)
    sentence = models.CharField(max_length=244)
    entities = models.JSONField()
    traits = models.JSONField()
    comment = models.CharField(max_length=244, null=True, blank=True)
    status = models.CharField(max_length=244)  # pending trained failed marked
    trained = models.IntegerField(default=0)
    weight = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'nlu_utterances'

    def __str__(self):
        return self.name
