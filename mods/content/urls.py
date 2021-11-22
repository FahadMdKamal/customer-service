from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mods.content.models.flow import Flow

from mods.content.views import ContentView, ContentCreateView, ContentDataView, ContentMediaView, ContentTaxonomyView, \
    ContentTextView, ConverseContentTypeView, ContentVarsView, ContentCustomFieldsView
from mods.content.views.flow import FlowView

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
router.register(r'flow', FlowView, basename="flow")

urlpatterns = [
    path('', include(router.urls)),
    path('create/', ContentCreateView.as_view()),
]