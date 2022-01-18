from email.policy import default
from hashlib import blake2b
from operator import mod
from xml.etree.ElementInclude import default_loader
from django.db import models
from .channel_typs import ChannelTypes


class MaverikChannels(models.Model):
    """
    Responsible for storing Mavrik Channel Types
    """

    CONNECTIVITY_STATUS = (
        ('active', 'Active'),
        ('expired', 'Expire'),
        ('paused', 'Paused'),
        ('retired', 'Retired'),
        ('unused', 'Unused'),
        ('active', 'Active'),
    )

    app_id = models.CharField(max_length=50, null=True, blank=True)
    channel_name = models.CharField(max_length=20, null=True, blank=True, unique=True)
    channel_ref = models.CharField(max_length=20, null=True, blank=True)
    channel_type = models.ForeignKey(ChannelTypes, on_delete=models.CASCADE, related_name="channel_type_set")
    details = models.JSONField(default=dict, null=True, blank=True)
    config = models.JSONField(default=dict, null=True, blank=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    connectivity_status = models.CharField(max_length=15, choices=CONNECTIVITY_STATUS, default='active')
    connectivity_note = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "mavrik_app_channels"
        verbose_name_plural = "Marik Channels"

    def __str__(self) -> str:
        return self.channel_name
