from django.contrib import admin

# Register your models here.
from mods.queue_service.models import QueueTopics


admin.site.register(QueueTopics)