from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from mods.content.models import Content


class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

class ContentNevItemSerializer(ModelSerializer):

    class Meta:
        model = Content
        fields = (
            'content_format',
            'title',
            'description',
            'action_items',
            'content_body',
            'parent_id'
            )
    
    def post(self, *args, **kwargs):
        pass


class ContentMenuDetailSerializer(ModelSerializer):
    nav_items = serializers.SerializerMethodField()
    menu_detail = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = (
            'content_format',
            'title',
            'description',
            'action_items',
            'content_body',
            'nav_items',
            'menu_detail'
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
        menu_objecs = []
        for item in childs:
            menu_objecs.append(ContentNevItemSerializer(item).data)
            
        return menu_objecs

    def get_menu_detail(self, instance):
        return {
            "menu":"", 
            "nav_items":"",
            "config":{
                "show-images":"",
                "menu-item":""
                }
            }
    
    def post(self, *args, **kwargs):
        pass
