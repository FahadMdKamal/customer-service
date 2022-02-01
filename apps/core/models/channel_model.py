from django.db import models

from django_mailbox.models import Mailbox


class Channels(models.Model):
    """
    Responsible for storing Mavrik Channel Types
    """

    CONNECTIVITY_STATUS = (
        ('active', 'Active'),
        ('expired', 'Expire'),
        ('paused', 'Paused'),
        ('retired', 'Retired'),
        ('unused', 'Unused'),
        ('inactive', 'Inactive'),
    )
    STATUS  = (
        (True, 'Active'), 
        (False, 'Inactive')
        )
    CH_TYPES = (
        ('facebook_page', 'Facebook Page'), 
        ('facebook_messenger', 'Facebook Messenger'),
        ('live_chat', 'Live Chat'),
        ('whatsapp', 'WhatsApp'),
        ('API', 'API'),
        ('email', 'Email'),
        )

    app_id = models.CharField(max_length=50, null=True, blank=True)
    channel_name = models.CharField(max_length=100, unique=True)
    channel_ref = models.CharField(max_length=20, null=True, blank=True)
    channel_type = models.CharField(max_length=40, choices=CH_TYPES)
    details = models.JSONField(default=dict, null=True, blank=True)
    mail_box = models.OneToOneField(Mailbox, on_delete=models.CASCADE, null=True, blank=True, related_name="channel_mail_box")
    config = models.JSONField(default=dict, null=True, blank=True)
    status = models.BooleanField(choices=STATUS, default=True)
    connectivity_status = models.CharField(max_length=15, choices=CONNECTIVITY_STATUS, default=True)
    connectivity_note = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "core_channel"
        verbose_name_plural = "Marik Channels"

    def __str__(self) -> str:
        return self.channel_name
    