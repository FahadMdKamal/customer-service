from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserAllowOrigin(models.Model):
    CIDR = (
        ('referrer', 'Referrer'),
        ('cidr', 'CIDR'),
        ('cookie', 'Cookie'),
    )
    PRINCIPLE = (
        ('apikey', 'API Key'),
        ('username', 'User Name'),
    )

    app_id = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='origin_user')
    principal = models.CharField(max_length=15, choices=PRINCIPLE, default='username')
    token = models.CharField(max_length=255, null=True, blank=True)
    origin_type = models.CharField(max_length=15, choices=CIDR, default='cidr')
    origin_sig = models.CharField(max_length=20, null=True, blank=True, default='0.0.0.0')
    expire_at = models.DateTimeField(default=datetime.now() + timedelta(days=7))
    allowed = models.BooleanField(default=False)
    last_seen_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_allowed_origins'

@receiver(post_save, sender=get_user_model())
def create_user_allow_origin(sender, **kwargs):
    if kwargs['created']:
        user_origin_obj = UserAllowOrigin(user=kwargs['instance'])
        user_origin_obj.save()