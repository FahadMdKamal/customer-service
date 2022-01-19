from django.urls import path, include
from mods.queue_service.views import TopicCreate,TopicStatusUpdate,TopicList,TopicReset


urlpatterns = [
    path('topic/create', TopicCreate.as_view()),
    path('topic/change_status',TopicStatusUpdate.as_view()),
    path('topic/list',TopicList.as_view()),
    path('topic/reset',TopicReset.as_view()),
]