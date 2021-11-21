from django.urls import path

from .views import ConverseContentTypeView
from .views.content import ContentView, ContentCreateView
from .views.content_data import ContentDataView
from .views.content_media import ContentMediaView
from .views.content_taxonomy import ContentTaxonomyView
from .views.content_text import ContentTextView
from .views.content_vars import ContentVarsView
from .views.custom_content_field import ContentCustomFieldsView


urlpatterns = [
    path('content/', ContentView.as_view({
        'get': 'list',
        'post': 'create'
    }), name="convo_content"),
    path('create/', ContentCreateView.as_view(), name="convo_content_create"),
    path('content_data/', ContentDataView.as_view({
        'get': 'list',
        'post': 'create'
    }), name="convo_content_data"),
    path('content_media/', ContentMediaView.as_view({
        'get': 'list',
        'post': 'create'
    }), name="convo_content_media"),
    path('content_taxonomy/', ContentTaxonomyView.as_view({
        'get': 'list',
        'post': 'create'
    }), name="convo_content_taxonomy"),
    path('content_text/', ContentTextView.as_view({
        'get': 'list',
        'post': 'create'
    }), name="convo_content_text"),
    path('content_type/', ConverseContentTypeView.as_view({
        'get': 'list',
        'post': 'create'
    }), name="convo_content_type"),
    path('content_vars/', ContentVarsView.as_view({
        'get': 'list',
        'post': 'create'
    }), name="convo_content_vars"),
    path('content_custom/', ContentCustomFieldsView.as_view({
        'get': 'list',
        'post': 'create'
    }), name="convo_content_custom_fields")
]
