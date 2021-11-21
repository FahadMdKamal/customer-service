from django.db import models


class StaticDictionary(models.Model):
    term_type = models.CharField(max_length=244)
    term_context = models.CharField(max_length=244, null=True, blank=True)
    term_value = models.CharField(max_length=244)
    order = models.IntegerField(default=0)

    class Meta:
        db_table = 'nlu_static_dictionary'
