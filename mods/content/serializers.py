from django.contrib.sessions.backends import file
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from mods.content.models.content import Content
from mods.content.models.content_data import ContentData
from mods.content.models.content_media import ContentMedia
from mods.content.models.content_taxonomy import ContentTaxonomy
from mods.content.models.content_text import ContentText
from mods.content.models.content_type import ConverseContentType
from mods.content.models.content_vars import ContentVars
from mods.content.models.custom_content_field import ContentCustomFields
from mods.content.models.content_options import ContentOptions
from mods.content.models.flow import Flow
from mods.content.models.flow_node import FlowNode
from mods.content.models.node_config import NodeConfig
from mods.content.models.node_contents import NodeContent


class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class ContentDataSerializer(ModelSerializer):
    class Meta:
        model = ContentData
        fields = '__all__'


class ContentMediaSerializer(ModelSerializer):
    class Meta:
        model = ContentMedia
        fields = '__all__'


class ContentTaxonomySerializer(ModelSerializer):
    class Meta:
        model = ContentTaxonomy
        fields = '__all__'


class ContentTextSerializer(ModelSerializer):
    class Meta:
        model = ContentText
        fields = '__all__'


class ConverseContentTypeSerializer(ModelSerializer):
    class Meta:
        model = ConverseContentType
        fields = '__all__'


class ContentVarsSerializer(ModelSerializer):
    class Meta:
        model = ContentVars
        fields = '__all__'


class CustomContentFieldSerializer(ModelSerializer):
    class Meta:
        model = ContentCustomFields
        fields = '__all__'


# Create Content Serializer

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


class FlowSerializer(ModelSerializer):
    class Meta:
        model = Flow
        fields = ('id', 'name', 'app_id', 'group')


class FlowNodeSerializer(ModelSerializer):
    config = serializers.JSONField(write_only=True)

    class Meta:
        model = FlowNode
        fields = ('id', 'name', 'flow', 'node_type', 'config')

    def create(self, validated_data):
        """
        Create and return a new `FlowNode` instance, given the validated data.
        """
        config = validated_data.pop('config')
        flow_node = FlowNode.objects.create(**validated_data)
        for key, value in config.items():
            node_config = NodeConfig(flow_node=flow_node, key=key, value=value)
            node_config.save()
        return flow_node

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.flow = validated_data.get('flow', instance.flow)
        instance.node_type = validated_data.get('node_type', instance.node_type)
        print(instance)
        instance.save()
        # id = validated_data.get('id', instance.id)
        # config = validated_data.get('config', instance.config)
        # for key, value in config.items():
        #     try:
        #         node_config = NodeConfig.objects.filter(flow_node_id=id, key=key).update(flow_node=id, key=key, value=value)
        #         node_config.save()
        #     except:
        #         pass

        return instance


class NodeConfigSerializer(ModelSerializer):
    class Meta:
        model = NodeConfig
        fields = ('id', 'flow_node', 'key', 'value')


class NodeContentSerializer(ModelSerializer):
    class Meta:
        model = NodeContent
        fields = ('id', 'flow_node', 'content')


# Flow nodes details get serializer
class NodeConfigDetailsSerializer(ModelSerializer):
    class Meta:
        model = NodeConfig
        fields = ('id', 'flow_node', 'key', 'value')


class FlowNodeDetailsSerializer(ModelSerializer):
    nodeconfigs = NodeConfigDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = FlowNode
        fields = ('id', 'name', 'flow', 'node_type', 'nodeconfigs')


class FlowDetailsSerializer(ModelSerializer):
    # flownodes = serializers.StringRelatedField(many=True)
    flownodes = FlowNodeDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Flow
        fields = ("id", "name", "app_id", "group", "flownodes")
        depths = 1
