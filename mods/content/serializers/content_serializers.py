from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from mods.content.models import Content, content


class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

class ContentNevItemSerializer(ModelSerializer):

    class Meta:
        model = Content
        exclude = (
            'type_ref',
            'app_id',
            'left_contents',
            'content_format',
            'template_cache',
            'value_cache',
            'subtitle',
            'last_used_at',
            )
    
    def post(self, *args, **kwargs):
        pass


class ContentMenuDetailSerializer(ModelSerializer):
    nav_items = serializers.SerializerMethodField()

    class Meta:
        model = Content
        exclude = (
            'type_ref',
            'app_id',
            'left_contents',
            'content_format',
            'template_cache',
            'value_cache',
            'subtitle',
            'last_used_at',
            )

    def get_nav_items(self, instance):
        childs = []
        items = Content.objects.filter(parent_id=instance)

        for item in items:
            childs.append(item)

        for item in items:
            ch = Content.objects.filter(parent_id=item)
            if ch.count() > 0:
                for c in ch:
                    childs.append(c)
        
        objs = []
            
        for item in childs:
            objs.append(ContentNevItemSerializer(item).data)

        return {"total-childs": len(objs), 'children': objs}
    
    def post(self, *args, **kwargs):
        pass
