from django.contrib import admin
from django import forms
from mods.queue_service.models import QueueTopics,QueuePrinciples,QueueItems
from apps.core.models import MaverikChannels


admin.site.register(QueueTopics)
admin.site.register(QueuePrinciples)

class QueueItemsForm(forms.ModelForm):
    class Meta:
        model = QueueItems
        fields = "__all__"
        
    def clean_app_id(self):
        app_id = self.cleaned_data['app_id']
        if not MaverikChannels.objects.filter(app_id=app_id).exists():
            raise forms.ValidationError("App with this id does not exists")
        return app_id

@admin.register(QueueItems)
class QueueItemsAdmin(admin.ModelAdmin):
    form = QueueItemsForm

