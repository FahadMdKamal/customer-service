from django.urls import path
from .views import MavrikAppApiView, MavrikAppCreateOrUpdateApiView, MevrikAppDeleteApiView, MavrikChannelsApiView, MevrikChannelDeleteApiView


urlpatterns = [
    path('list/', MavrikAppApiView.as_view()),
    path('create-update/', MavrikAppCreateOrUpdateApiView.as_view()),
    path('delete/', MevrikAppDeleteApiView.as_view()),
    path('channel/create-update-list/', MavrikChannelsApiView.as_view()),
    path('channel/delete/', MevrikChannelDeleteApiView.as_view()),

]
