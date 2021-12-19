from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class LoggedInUserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="logged_info")
    os = models.CharField(max_length=50)
    browser = models.CharField(max_length=100)
    ip = models.CharField(max_length=40)
    hash = models.CharField(max_length=255)
    is_allowed = models.BooleanField(default=False)
    