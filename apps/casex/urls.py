from django.urls import path
from django.urls.conf import include
from .views import CaseMessageAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', CaseMessageAPIView, basename="casex-case-message")
app_name = "casex_case"

urlpatterns = [
    path('case-message/', include(router.urls)),

]
