from django.contrib import admin

# Register your models here.
from mods.queue_service.models import QueueTopics,QueuePrinciples,QueueItems


admin.site.register(QueueTopics)
admin.site.register(QueuePrinciples)
admin.site.register(QueueItems)