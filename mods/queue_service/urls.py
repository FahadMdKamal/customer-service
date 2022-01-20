from django.urls import path, include
from mods.queue_service.views import (TopicCreate,TopicStatusUpdate,QueueItemRemove,
TopicList,TopicReset,QueueItemPublish,QueueItemList)




urlpatterns = [
    # Queue Topic
    path('topic/create', TopicCreate.as_view()),
    path('topic/change_status',TopicStatusUpdate.as_view()),
    path('topic/list',TopicList.as_view()),
    path('topic/reset',TopicReset.as_view()),

    # Queue Items
    path('item/publish',QueueItemPublish.as_view()),  # For any type update use patch
    path('item/remove',QueueItemRemove.as_view()),
    path('item/list',QueueItemList.as_view())
    
]