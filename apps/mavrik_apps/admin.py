from django.contrib import admin
from .models import MavrikApps, ChannelTypes, MaverikChannels


admin.site.register(ChannelTypes)
admin.site.register(MavrikApps)

admin.site.register(MaverikChannels)