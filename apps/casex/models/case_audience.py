from django.db import models

from .case_message import CaseMessage, CaseId

class CaseAudience(models.Model):
    case_id = models.ForeignKey(CaseId, on_delete=models.CASCADE,related_name="audiance_case_id")
    source_message = models.ForeignKey(CaseMessage, on_delete=models.CASCADE, related_name='audience_case_message', null=True, blank=True)
    audience_type = models.CharField(max_length=50, null=True, blank=True)
    audience_role = models.CharField(max_length=50, null=True, blank=True)
    audience_ref = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    ref_code = models.CharField(max_length=100,null=True, blank=True)
    
    internal_id = models.IntegerField(default=0)
    external_id = models.IntegerField(default=0)
    body = models.TextField()
    photo_url = models.URLField(null=True, blank=True)
    origin_channel_id = models.IntegerField(default=0)
    details = models.JSONField(default=dict, null= True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True)
    access_expire_at = models.DateTimeField(null= True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "casex_case_audience"
        