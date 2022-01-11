from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from mods.content.models import Content


class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class ContentNevItemSerializer(ModelSerializer):
    """
    Represents Childens of the Parent menu
    """

    class Meta:
        model = Content
        fields = ('id',
                  'content_format',
                  'title',
                  'description',
                  'action_items',
                  'content_body', 
                  'parent_id',)


class ContentMenuDetailSerializer(ModelSerializer):
    """
    Representing Content Menu detial according with childrens
    """
    nav_items = serializers.SerializerMethodField()
    menu_detail = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = ('id',
                  'content_format',
                  'title',
                  'description',
                  'action_items',
                  'content_body',
                  'nav_items',
                  'menu_detail')

    def extract_item(self, nav_obj, nav_list: list):
        """
        Recursively call and check if there is any child available.
        """
        cont = Content.objects.filter(parent_id=nav_obj)
        if len(cont) == 0:
            return nav_list
        else:
            for ct in cont:
                nav_list.append(ct)
                self.extract_item(ct, nav_list)
            return nav_list

    def get_nav_items(self, instance):
        """
        Get all the children for the model object
        """
        childs = self.extract_item(instance, [])
        menu_objecs = []
        for item in childs:
            menu_objecs.append(ContentNevItemSerializer(item).data)
        return menu_objecs

    def get_menu_detail(self, instance):
        """
        Responsible for showing menu detail fields data to menu detail serializer field.
        """
        return {
            "menu": "",
            "nav_items": "",
            "config": {
                "show-images": "",
                "menu-item": ""
            }
        }
            