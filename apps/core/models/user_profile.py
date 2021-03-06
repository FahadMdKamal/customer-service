from django.db import models
from django.contrib.auth import get_user_model

from .apps_model import Apps
from django.db.models.signals import post_save
from django.dispatch import receiver

app_user_model = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        app_user_model, on_delete=models.CASCADE, related_name="profile_data")
    profile_image = models.ImageField(
        upload_to="profile", null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    allowed_apps = models.ManyToManyField(
        Apps, related_name="user_apps", blank=True)
    login_attempts = models.IntegerField(default=0)

    class Meta:
        db_table = "core_user_profiles"


@receiver(post_save, sender=app_user_model)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile(user=kwargs['instance'])
        profile.save()
