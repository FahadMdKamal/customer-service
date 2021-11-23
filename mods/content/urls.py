from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mods.content.models.flow import Flow

from mods.content.views import ContentView, ContentCreateView, ContentDataView, ContentMediaView, ContentTaxonomyView, \
    ContentTextView, ConverseContentTypeView, ContentVarsView, ContentCustomFieldsView, FlowCreateOrUpdateView, \
    FlowListView, FlowDeleteView, AddNodeView, AddNodeConfigView, UpdateNodeView, AttachContentView, DeleteContentView, FlowNodeView

router = DefaultRouter()

router.register(r'content', ContentView, basename="content")
# router.register(r'create', ContentCreateView.as_view(), basename="convo_content_create"),
router.register(r'content_data', ContentDataView, basename="convo_content_data"),
router.register(r'content_media', ContentMediaView, basename="convo_content_media"),
router.register(r'content_taxonomy', ContentTaxonomyView, basename="convo_content_taxonomy"),
router.register(r'content_text', ContentTextView, basename="convo_content_text"),
router.register(r'content_type', ConverseContentTypeView, basename="convo_content_type"),
router.register(r'content_vars', ContentVarsView, basename="convo_content_vars"),
router.register(r'content_custom', ContentCustomFieldsView, basename="convo_content_custom_fields")
# router.register(r'flow', FlowCreateOrUpdateView, basename="flow")

urlpatterns = [
    path('', include(router.urls)),
    path('create/', ContentCreateView.as_view()),
    path('flow-create-update/', FlowCreateOrUpdateView.as_view()),
    path('flow-list/', FlowListView.as_view()),
    path('flow-delete/', FlowDeleteView.as_view()),
    path('add-node/', AddNodeView.as_view()),
    path('flow-node/', FlowNodeView.as_view()),
    path('update-node/', UpdateNodeView.as_view()),
    path('add-node-config/', AddNodeConfigView.as_view()),
    # path('update-node-config/', UpdateNodeView.as_view()),
    path('attach-content/', AttachContentView.as_view()),
    path('delete-content/', DeleteContentView.as_view()),
]