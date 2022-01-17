from django.urls import path

from .views import MavrikAppApiView

urlpatterns = [

    path('list/', MavrikAppApiView.as_view(),)

]
