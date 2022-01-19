from django.db import models


class ChannelTypes(models.Model):
    """
    Responsible for storing Mavrik Channel Types
    """
    channel_name = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "marik_channels"
        verbose_name_plural = "Marik Channels"

    def __str__(self) -> str:
        return self.channel_name
