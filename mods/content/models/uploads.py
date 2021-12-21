from django.db import models
import os, uuid, datetime

class FileManager:
    ''' Will manage files and photos '''
    @staticmethod
    def photo_path(instance, filename):

        basefilename, file_extension = os.path.splitext(filename)
        folder = file_extension.replace(".", "").upper()
        date = datetime.datetime.today()
        uid = uuid.uuid4()
        return f'app-{instance.app_id}/{folder}/{uid}{file_extension}'


class Upload(models.Model):
    app_id = models.IntegerField(default=0)
    owner = models.CharField(max_length=100,null=True, blank=True)
    storage = models.CharField(max_length=255, null=True, blank=True, default="Local")
    filepath = models.FileField(upload_to=FileManager.photo_path, null=True, blank=True)
    resource_type = models.CharField(max_length=100, null=True, blank=True)
    display_name = models.CharField(max_length=100, null=True, blank=True)
    filemeta = models.JSONField(default=dict, null=True, blank=True)
    variation = models.JSONField(default=dict, null=True, blank=True)
    details = models.JSONField(default=dict, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'content_uploads'

    @property
    def secure_url(self):
        return self.filepath.url
