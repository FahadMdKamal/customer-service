from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
import markdown

from mods.content.models import MessageTemplate


class MessageTemplateSerializer(ModelSerializer):
    template_code = serializers.CharField(required=False)
    template = serializers.SerializerMethodField()

    class Meta:
        model = MessageTemplate
        fields =  "__all__"

    def get_template(self, instance):

        if instance.template_format == 'markdown':
            result = markdown.markdown(instance.body_template)
            return result
