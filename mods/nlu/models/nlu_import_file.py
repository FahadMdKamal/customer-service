from django.db import models
from .nlu_intent import NluIntent


class NluImportFile(models.Model):
    utterances = models.CharField(max_length=244)
    intent = models.ForeignKey(NluIntent, blank=True, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "nlu_import_file"
