from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MavrikAppApiView, MavrikAppCreateOrUpdateApiView, MevrikAppDeleteApiView, MavrikChannelsApiView

router = DefaultRouter()

router.register('mavrik-channels', MavrikChannelsApiView, basename='mavrik-channels')


urlpatterns = [
    path('', include(router.urls)),
    path('list/', MavrikAppApiView.as_view()),
    path('create-update/', MavrikAppCreateOrUpdateApiView.as_view()),
    path('delete/', MevrikAppDeleteApiView.as_view())

]
