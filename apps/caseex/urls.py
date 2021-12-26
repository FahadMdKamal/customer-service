from os import name
from django.urls import path
from .views import CaseMessageAPIView

app_name = "caseex_case"

urlpatterns = [
    path('case-message/', CaseMessageAPIView.as_view(), name="caseex_case_message"),

]
