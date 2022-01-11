from django.contrib import admin
from apps.casex.models import CaseId, CaseMessage, CaseAudience

admin.site.register(CaseId)
admin.site.register(CaseMessage)
admin.site.register(CaseAudience)