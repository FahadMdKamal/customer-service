from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_mailbox.models import Mailbox

from .apps_model import Apps


class Channels(models.Model):
    """
    Responsible for storing mevrik Channel Types
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

    app = models.ForeignKey(Apps, on_delete=models.CASCADE, related_name="channel_app")
    channel_name = models.CharField(max_length=100)
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
        unique_together = ('app', 'channel_name')

    def __str__(self) -> str:
        return self.channel_name


@receiver(post_save, sender=Channels)
def create_channel_mailbox(sender, **kwargs):
    """
    - If email type channel is created create mailbox.
    - If channel is updated and is email type check if mailbox exist ?
    - If mailbox doesn't exit create one else update existing.
    """
    if kwargs['created'] and kwargs['instance'].channel_type == 'email':
        channel = kwargs['instance']
        mbox = Mailbox.objects.create(name=kwargs['instance'].channel_name)
        channel.mail_box = mbox
        channel.save()
    else:
        channel = kwargs['instance']
        if channel.channel_type == 'email' and not channel.mail_box:
            mbox = Mailbox.objects.create(name=channel.channel_name)
            channel.mail_box = mbox
            channel.save()

        elif channel.channel_type == 'email' and channel.mail_box:
            channel.mail_box.name = channel.channel_name
            channel.mail_box.save()
