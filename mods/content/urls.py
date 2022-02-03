from django.urls import path, include
from rest_framework.routers import DefaultRouter

from mods.content.views import ContentView, ContentCreateView, ContentDataView, ContentMediaView, ContentTaxonomyView, \
    ContentTextView, ConverseContentTypeView, ContentVarsView, ContentCustomFieldsView, FlowCreateOrUpdateView, \
    FlowListView, FlowDeleteView, AttachContentView, DeleteContentView, \
    FlowNodeView, CreateUpdateNodeConfigView, SingleContentDetailsView, ContentTextModelView, ContentTextSearchView, \
    FlowNodeDeleteView, NodeListView, ContentDeleteView, MenuDetailAPIView
from mods.content.views.flow import FlowDetailsView, FlowIntent
from mods.content.views import MessageTemplateCreateOrUpdateView, MessageTemplateDetailsView, MessageTemplateDeleteView, MessageTemplateListView

router = DefaultRouter()

router.register(r'content_list', ContentView, basename="content")
router.register(r'csat_list', ContentView, basename="csat")
# router.register(r'create', ContentCreateView.as_view(), basename="convo_content_create"),
router.register(r'content_data', ContentDataView, basename="convo_content_data"),
router.register(r'content_media', ContentMediaView, basename="convo_content_media"),
router.register(r'content_taxonomy', ContentTaxonomyView, basename="convo_content_taxonomy"),
router.register(r'content_text', ContentTextModelView, basename="convo_content_text"),
router.register(r'content_type', ConverseContentTypeView, basename="convo_content_type"),
router.register(r'content_vars', ContentVarsView, basename="convo_content_vars"),
router.register(r'content_custom', ContentCustomFieldsView, basename="convo_content_custom_fields")
router.register(r'node-list', NodeListView, basename="flow_node_list")
router.register(r'flow-list', FlowListView, basename="flow_list")
# router.register(r'flow', FlowCreateOrUpdateView, basename="flow")


urlpatterns = [
    path('', include(router.urls)),
    path('content-create-update/', ContentCreateView.as_view()),
    path('content-delete/', ContentDeleteView.as_view()),

    path('menu/', MenuDetailAPIView.as_view()),

    path('csat-delete/', ContentDeleteView.as_view()),
    path('csat-create-update/', ContentCreateView.as_view()),
    # path('csat-list/', ContentView.as_view()),
    path('text-create-update/', ContentTextView.as_view()),
    path('text-search/', ContentTextSearchView.as_view()),
    path('single-content-details/', SingleContentDetailsView.as_view()),
    path('single-csat-details/', SingleContentDetailsView.as_view()),
    path('flow-create-update/', FlowCreateOrUpdateView.as_view()),
    # path('flow-list/', FlowListView.as_view()),
    path('flow-delete/', FlowDeleteView.as_view()),
    path('intent-flow/', FlowIntent.as_view()),
    path('node-create-update/', FlowNodeView.as_view()),
    path('node-delete/', FlowNodeDeleteView.as_view()),
    path('node-mevrik-create-update/', CreateUpdateNodeConfigView.as_view()),
    path('attach-content/', AttachContentView.as_view()),
    path('delete-content/', DeleteContentView.as_view()),
    path('delete-csat/', DeleteContentView.as_view()),
    path('single_flow_details/', FlowDetailsView.as_view()),

    path('message-template-create-update/', MessageTemplateCreateOrUpdateView.as_view()),
    path('message-template-detail/', MessageTemplateDetailsView.as_view()),
    path('message-template-list/', MessageTemplateListView.as_view()),
    path('message-template-delete/', MessageTemplateDeleteView.as_view()),
]



    # path('', include(router.urls)),
    
    # # supported actions create, list, delete, ecport 
    # path('action/<string:model>/<string:action>', ContentCreateView.as_view()),

    # # action/csat/list { data: { cast_type: 'urgent' } }
    # # action/csat/delete { data: { id: 1 } }

    # # action/csat { action: "list", data: { cast_type: 'urgent' } }
    # # action/csat { action: "delete", data: { cast_type: 'urgent' } }


    # path('cast/<string:action>', ContentCreateView.as_view()),

    # # csat/list { cast_type: 'urgent' }
    # # csat/delete { id: 1 }

