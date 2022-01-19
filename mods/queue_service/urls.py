from django.urls import path, include
from mods.queue_service.views import TopicCreate

urlpatterns = [
    path('topic/create', TopicCreate.as_view()),
]