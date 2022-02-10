from django.urls import path, include
from rest_framework.routers import DefaultRouter

from mods.nlu.views import RetrainView, NluImportDataView, NluEntitiesViewSet, StaticDictionaryViewSet, \
    NluIntentGroupViewSet, NluIntentUtterViewSet, NluIntentViewSet, NluUtteranceViewSet, NluLookupViewSet, \
    NluSyncViewSet, UtteranceUploadData, MessageView, NluUtterancesConfidenceView, NluUtterancesFullTextSearchView, \
    SyncIntent, SyncEntities, SyncTraits, SyncUtterances, UtteranceTrainStatus, ExtratorViewSet

router = DefaultRouter()

# NLP api's
router.register(r'retrain', RetrainView, basename="retrain")
router.register(r'import', NluImportDataView, basename="import")
router.register(r'entities', NluEntitiesViewSet, basename="entities")
router.register(r'intent_terms', StaticDictionaryViewSet, basename="intent_terms")
router.register(r'intent_group', NluIntentGroupViewSet, basename="intent_group")
router.register(r'intent', NluIntentViewSet, basename="intent")
router.register(r'intent_get_details', NluIntentUtterViewSet, basename="intent_get_details")
router.register(r'utterances', NluUtteranceViewSet, basename="utterances")
router.register(r'lookup', NluLookupViewSet, basename="lookup")
router.register(r'intent_sync', NluSyncViewSet, basename="intent_sync")
router.register(r'file_utterances', UtteranceUploadData, basename="file_utterances")
router.register(r'message', MessageView, basename="message")
router.register(r'confidence_score', NluUtterancesConfidenceView, basename="confidence_score")
router.register(r'search', NluUtterancesFullTextSearchView, basename="search")
# sync
router.register(r'sync/intent', SyncIntent, basename="intent_sync")
router.register(r'sync/entities', SyncEntities, basename="entities_sync")
router.register(r'sync/traits', SyncTraits, basename="traits_sync")
router.register(r'sync/utterances', SyncUtterances, basename="utterances_sync")
router.register(r'sync/utterances_status', UtteranceTrainStatus, basename="utterances_status")
router.register(r'extract', ExtratorViewSet, basename="extractorViewSet")

urlpatterns = [
    path('', include(router.urls)),
]
