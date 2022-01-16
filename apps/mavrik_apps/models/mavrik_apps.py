from django.db import models
from .mavrik_channel_typs import ChannelTypes

class MavrikApps(models.Model):
    """
    Responsible for storing Mavrik Apps
    """
    STATUS  = (
        ('active', 'Active'), 
        ('inactive', 'Inactive')
        )

    app_code = models.CharField(max_length=20, unique=True)
    app_domain = models.CharField(max_length=255, null=True, blank=True)
    app_config = models.JSONField(default=dict, null=True, blank=True)
    app_icon = models.CharField(max_length=20, null=True, blank=True)
    allowed_domains = models.JSONField(default=dict, null=True, blank=True)
    allowed_channel_types = models.ManyToManyField(ChannelTypes, related_name="app_channels", blank=True )
    status = models.CharField(choices=STATUS, max_length=10, default='inactive')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "mavrik_apps"
        verbose_name_plural = "Mavrik Apps"

    def __str__(self) -> str:
        return self.app_code
    
    def save(self):
        self.app_code = self.app_code.strip().upper()
        if self.app_domain:
            self.app_domain = self.app_domain.strip().lower()
        return super().save()

