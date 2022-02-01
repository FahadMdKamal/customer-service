from django.db import models
from django.contrib.auth import get_user_model

app_user_model = get_user_model()

ROLE = (
    ('admin', 'Admin'),
    ('manager', 'Manager'),
    ('supervisor', 'Supervisor'),

)


class WorkGroups(models.Model):
    user = models.ManyToManyField(
        app_user_model, related_name="work_group_user")
    user_role = models.CharField(
        choices=ROLE,
        default='admin',
        null=True,
        blank=True,
        max_length=50
    )
    permissions = models.JSONField(null=True, blank=True)
    active_since = models.DateTimeField(null=True, blank=True)
    user_workgroups = models.JSONField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Work Groups'
        db_table = 'core_work_group'

    @property
    def workgroup_id(self):
        return self.id
