from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.shortcuts import get_object_or_404

from mods.content.models import MessageTemplate, Upload


class MessageTemplateSerializer(ModelSerializer):
    template_code = serializers.CharField(required=False)
    file = serializers.FileField(required=False)

    class Meta:
        model = MessageTemplate
        fields = "__all__"
        
        read_only_fields = ('attachments',)
        
    def create(self, validated_data):
        file = validated_data.pop("file", None)
        if file:
            obj = Upload(
                app_id=validated_data['app_id'],
                owner=validated_data['owner'],
                filepath=file
                )
            obj.save()
            validated_data['attachments'] = {"id":obj.id,"url":obj.secure_url}
        return super().create(validated_data)

    def update(self, instance, validated_data):
        file = validated_data.pop("file", None)
        
        if file:
            attachment_id = instance.attachments.get('id')
            attachment_obj_url = instance.attachments.get('url')
            upload_obj = get_object_or_404(Upload, id=attachment_id)

            print(instance.attachments)
            
            if Upload.objects.filter(id=attachment_id).exists():
                print("update")
                obj_id = Upload.objects.filter(id=attachment_id).update(
                    app_id=validated_data['app_id'],
                    owner=validated_data['owner'],
                    filepath=file
                    )
                obj = Upload.objects.get(id=obj_id)
            else:
                obj = Upload(
                    app_id=validated_data['app_id'],
                    owner=validated_data['owner'],
                    filepath=file
                    )
            obj.save()
            
            validated_data['attachments'] = {"id":obj.id,"url":obj.secure_url}
        
        return super().update(instance, validated_data)
