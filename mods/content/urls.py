from django.urls import path, include
from rest_framework.routers import DefaultRouter

from mods.content.views import ContentView, ContentCreateView, ContentDataView, ContentMediaView, ContentTaxonomyView, \
    ContentTextView, ConverseContentTypeView, ContentVarsView, ContentCustomFieldsView, FlowCreateOrUpdateView, \
    FlowListView, FlowDeleteView, AddNodeView, UpdateNodeView, AttachContentView, DeleteContentView, \
    FlowNodeView, CreateUpdateNodeConfigView, SingleContentDetailsView, ContentTextModelView
from mods.content.views.flow import FlowDetailsView

router = DefaultRouter()

router.register(r'content', ContentView, basename="content")
# router.register(r'create', ContentCreateView.as_view(), basename="convo_content_create"),
router.register(r'content_data', ContentDataView, basename="convo_content_data"),
router.register(r'content_media', ContentMediaView, basename="convo_content_media"),
router.register(r'content_taxonomy', ContentTaxonomyView, basename="convo_content_taxonomy"),
router.register(r'content_text', ContentTextModelView, basename="convo_content_text"),
router.register(r'content_type', ConverseContentTypeView, basename="convo_content_type"),
router.register(r'content_vars', ContentVarsView, basename="convo_content_vars"),
router.register(r'content_custom', ContentCustomFieldsView, basename="convo_content_custom_fields")
# router.register(r'flow', FlowCreateOrUpdateView, basename="flow")

urlpatterns = [
    path('', include(router.urls)),
    path('content-create-update/', ContentCreateView.as_view()),
    path('text-create-update/', ContentTextView.as_view()),
    path('single-content-details/', SingleContentDetailsView.as_view()),
    path('flow-create-update/', FlowCreateOrUpdateView.as_view()),
    path('flow-list/', FlowListView.as_view()),
    path('flow-delete/', FlowDeleteView.as_view()),
    path('node-create-update/', AddNodeView.as_view()),
    path('flow-node/', FlowNodeView.as_view()),
    path('update-node/', UpdateNodeView.as_view()),
    path('node-config-create-update/', CreateUpdateNodeConfigView.as_view()),
    path('attach-content/', AttachContentView.as_view()),
    path('delete-content/', DeleteContentView.as_view()),

    path('single_flow_details/', FlowDetailsView.as_view()),
]