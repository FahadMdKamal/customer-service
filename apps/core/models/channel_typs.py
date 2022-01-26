from django.db import models


class ChannelTypes(models.Model):
    """
    Responsible for storing Mavrik Channel Types
    """
    PLATFORMS = (
        ('facebook', 'Facebook'),
        ('whattsapp', 'WhattsApp'),
        ('gmail', 'Mail'),
    )
    channel_name = models.CharField(max_length=20, unique=True)
    platform = models.CharField(max_length=20, choices=PLATFORMS, default='facebook')
    icon = models.CharField(max_length=20, null=True, blank=True)
    label = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "core_mavrik_app_channel_type"
        verbose_name_plural = "Marik Channel Types"

    def __str__(self) -> str:
        return self.channel_name
