from django.db import models
from django.contrib.auth.models import Group
from django.utils.text import slugify


class Apps(models.Model):
    """
    Responsible for storing Mavrik Apps
    """
    STATUS  = (
        ('active', 'Active'), 
        ('inactive', 'Inactive')
        )
    CHANNEL_TYPE  = (
        ('facebook', 'Facebook'), 
        ('whatsapp', 'WhatsApp'),
        ('email', 'Email'),
        )

    app_code = models.CharField(max_length=20, unique=True)
    app_domain = models.CharField(max_length=255, null=True, blank=True)
    app_config = models.JSONField(default=dict, null=True, blank=True)
    app_icon = models.CharField(max_length=20, null=True, blank=True)
    allowed_domains = models.JSONField(default=dict, null=True, blank=True)
    allowed_channel_types = models.CharField(
        choices=CHANNEL_TYPE, 
        max_length=10, 
        default='facebook'
    )
    status = models.CharField(choices=STATUS, max_length=10, default='inactive')
    slug = models.SlugField(unique=True)
    groups = models.ManyToManyField(Group, related_name="app_groups")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "core_apps"
        verbose_name_plural = "Apps"

    def __str__(self) -> str:
        return self.app_code
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slugified= slugify((self.app_code,self.app_domain))
            count = 0
            new_slugified = slugified
            while Apps.objects.filter(slug=new_slugified).exists():
                count += 1
                new_slugified = slugified + str(count)
            self.slug = new_slugified
        self.app_code = self.app_code.strip().upper()
        if self.app_domain:
            self.app_domain = self.app_domain.strip().lower()
        return super(Apps, self).save(*args, **kwargs)


