from django.db import models


class ContentMedia(models.Model):
    media_type = models.CharField(max_length=100, default="image")
    media_ref = models.CharField(max_length=244, default="media/")
    file = models.FileField(upload_to='media/')
    storage_provider = models.CharField(max_length=100, default="local")
    status = models.CharField(max_length=244, default="active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.file:
            self.media_ref = self.file
        return super().save(*args, **kwargs)

    class Meta:
        db_table = 'converse_content_media'
