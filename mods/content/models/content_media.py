from django.db import models


class ContentMediaManager(models.Manager):
    pass


class ContentMedia(models.Model):
    media_type = models.CharField(max_length=100)
    media_ref = models.CharField(max_length=244)
    public_url = models.FileField(upload_to='media/')
    storage_provider = models.CharField(max_length=100)
    status = models.CharField(max_length=244)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ContentMediaManager()

    class Meta:
        db_table = 'converse_content_media'
