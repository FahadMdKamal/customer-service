from os import name
from django.urls import path
from django.urls.conf import include
from .views import CaseMessageAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', CaseMessageAPIView, basename="caseex-case-message")
app_name = "caseex_case"

urlpatterns = [
    path('case-message/', include(router.urls)),

]
