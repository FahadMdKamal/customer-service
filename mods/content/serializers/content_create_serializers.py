from rest_framework import serializers

from mods.content.models import (
    Content,
    ContentData,
    ContentOptions
)

class ContentCustomSerializer(serializers.Serializer):
    key = serializers.CharField(max_length=244)
    val = serializers.CharField(max_length=244)


class ContentOptionsSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=244)
    value = serializers.CharField(max_length=244)


class ContentCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=244)
    description = serializers.CharField(max_length=244)
    type_ref = serializers.CharField(max_length=244)
    subtitle = serializers.CharField(max_length=244)
    custom_fields = ContentCustomSerializer(many=True)
    options = ContentOptionsSerializer(many=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """

        content = Content(type_ref=validated_data["type_ref"],
                          title=validated_data["title"],
                          app_id=validated_data["app_id"],
                          subtitle=validated_data["subtitle"],
                          description=validated_data["description"],
                          default_action="action",
                          action_items={},
                          left_contents={},
                          display_order="0",
                          content_body=validated_data["description"],
                          content_format="JSON",
                          template_cache="CACHE",
                          value_cache="VALUE CACHE",
                          )
        content.save()
        for field in validated_data["custom_fields"]:
            key = field['key']
            val = field["val"]
            data = ContentData(
                content_id=content,
                field_key=key,
                field_value=val,
                params={}
            )
            data.save()

        for option in validated_data["options"]:
            option_name = option["type"]
            option_value = option["value"]
            optns = ContentOptions(
                content=content,
                option_name=option_name,
                option_value=option_value
            )
            optns.save()
        return validated_data
