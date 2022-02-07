from django.db import models
from django.contrib.auth import get_user_model

from apps.core.models.channel_model import Channels
# from .channel_model import Channels

app_user_model = get_user_model()

class WorkGroups(models.Model):

    ROLE = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('supervisor', 'Supervisor'),

    )
    user_role = models.CharField(
        choices=ROLE,
        default='admin',
        null=True,
        blank=True,
        max_length=50
    )
    channel = models.ForeignKey(Channels, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    user = models.ManyToManyField(
        app_user_model, related_name="work_group_user")
    permissions = models.JSONField(null=True, blank=True)
    active_since = models.DateTimeField(null=True, blank=True)
    user_workgroups = models.JSONField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Work Groups'
        db_table = 'core_work_group'
        unique_together = ('channel', 'name',)

    @property
    def workgroup_id(self):
        return self.id

    def __str__(self) -> str:
        return f'{self.name}--{self.channel.app}--{self.channel.channel_name}'