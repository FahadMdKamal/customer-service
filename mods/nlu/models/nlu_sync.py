from django.db import models

from . import NluIntent, NluEntities, NluUtterances, StaticDictionary

NLUTYPE = (
    ('intent', 'intent'),
    ('entities', 'entities'),
    ('traits', 'traits'),
    ('utterances', 'utterances'),
)


class NluSyncManager(models.Manager):

    def get_all_intent(self):
        return NluIntent.objects.order_by('-created_at')

    def get_all_entities(self):
        return NluEntities.objects.order_by('-created_at')

    def get_all_utterances(self):
        return NluUtterances.objects.order_by('-created_at')

    def get_all_traits(self):
        return StaticDictionary.objects.filter(term_type="traits")

    def utterance_trained_status(self, pk):
        return NluUtterances.objects.filter(pk=pk).update(status="trained")

    def single_intent_check(self, pk, owner_type):
        if NluSync.objects.filter(owner_id=pk, owner_type=owner_type).exists():
            return True
        else:
            return False

    def create_nlusync(self, owner_id, owner_type, property_request):
        q = NluSync(property_id="wit", owner_id=owner_id, owner_type=owner_type, property_request=property_request,
                    property_response={}, status="pending")
        q.save()
        return q


class NluSync(models.Model):
    property_id = models.CharField(max_length=244)
    owner_id = models.CharField(max_length=244, null=True, blank=True, default="wit")
    owner_type = models.CharField(choices=NLUTYPE, max_length=50, null=True)
    property_request = models.JSONField(null=True, blank=True)
    property_response = models.JSONField(null=True, blank=True)

    status = models.CharField(max_length=244)
    request_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = NluSyncManager()

    class Meta:
        db_table = 'nlu_sync'
