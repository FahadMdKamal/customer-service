from django.urls import path

from .views import MavrikAppApiView, MavrikAppCreateOrUpdateApiView

urlpatterns = [

    path('list/', MavrikAppApiView.as_view()),
    path('create-update/', MavrikAppCreateOrUpdateApiView.as_view())

]
