from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from mods.content.models import Content
from mods.content.models.content_options import ContentOptions
from mods.content.models.node_contents import NodeContent
from mods.content.serializers import ContentSerializer, ContentCreateSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import response

import json


class ContentView(ModelViewSet):
    serializer_class = ContentSerializer
    queryset = Content.objects.all().order_by('-id')
    http_method_names = ['get']

    def get_queryset(self):
        params = {}

        if self.request.query_params.get("app_id", None) is not None:
            params.update({"app_id": self.request.query_params["app_id"]})

        if self.request.query_params.get("content_type", None) is not None:
            params.update({"content_type": self.request.query_params["content_type"]})

        if self.request.query_params.get("node_id", None) is not None:
            params.update({"node_id": self.request.query_params["node_id"]})

        return Content.objects.filter(**params).order_by('-id')


class ContentCreateView(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            content_parent_id = Content.objects.filter(pk=data['parent_id']).exists()
            if content_parent_id:
                content_parent_id = content_parent_id
            else:
                content_parent_id = None
            # content save
            content_create = Content.objects.filter(id=data["id"]).update(type_ref=data["content_type"],
                                                                          app_id=data["app_id"],
                                                                          title=data["title"],
                                                                          subtitle=data["subtitle"],
                                                                          description=data["description"],
                                                                          default_action="",
                                                                          action_items=data["action_items"],
                                                                          parent_id=content_parent_id,
                                                                          left_contents="",
                                                                          display_order=data["display_order"],
                                                                          content_body=data["content_body"],
                                                                          content_format=data["content_format"],
                                                                          template_cache="",
                                                                          value_cache=""
                                                                          )
            # # content options save
            # for key, value in data["options"].items():
            #     content_options = ContentOptions(content=content_create,
            #                                      option_name=key,
            #                                      option_value=value)
            #     content_options.save()
            # # node content save
            # node_content = NodeContent(flow_node_id=data["node_id"],
            #                            content_id=content_create.id)
            # node_content.save()
            # # Content Media save
            return response.Response(data=data, status=status.HTTP_201_CREATED)
        else:
            content_parent_id = Content.objects.filter(pk=data['parent_id']).exists()
            if content_parent_id:
                content_parent_id = content_parent_id
            else:
                content_parent_id = None
            # content save
            content_create = Content(type_ref=data["content_type"],
                                     app_id=data["app_id"],
                                     title=data["title"],
                                     subtitle=data["subtitle"],
                                     description=data["description"],
                                     default_action="",
                                     action_items=data["action_items"],
                                     parent_id=content_parent_id,
                                     left_contents="",
                                     display_order=data["display_order"],
                                     content_body=data["content_body"],
                                     content_format=data["content_format"],
                                     template_cache="",
                                     value_cache=""
                                     )
            content_create.save()
            # content options save
            for key, value in data["options"].items():
                content_options = ContentOptions(content=content_create,
                                                 option_name=key,
                                                 option_value=value)
                content_options.save()
            # node content save
            try:
                node_content = NodeContent(flow_node_id=data["node_id"],
                                           content_id=content_create.id)
                node_content.save()
            except:
                pass
            # Content Media save
            data["id"] = content_create.id
            return response.Response(data=data, status=status.HTTP_201_CREATED)


class SingleContentDetailsView(APIView):

    def post(self, request):
        results = {}
        data = json.loads(request.body.decode('utf-8'))
        id = data['id']
        # content save
        content_create = Content.objects.filter(id=id).first()
        results.update({'id': id})
        try:
            results.update({"node_id": NodeContent.objects.filter(content_id=id).first().flow_node.id})
        except:
            pass
        option = {}
        for i in ContentOptions.objects.filter(content=id):
            option.update({i.option_name: i.option_value})
        results.update(options=option)
        results.update(content_type=content_create.type_ref,
                       app_id=content_create.app_id,
                       title=content_create.title,
                       subtitle=content_create.subtitle,
                       description=content_create.description,
                       action_items=content_create.action_items,
                       parent_id=content_create.parent_id,
                       display_order=content_create.display_order,
                       content_body=content_create.content_body,
                       content_format=content_create.content_format,
                       )

        return response.Response(data=results, status=status.HTTP_201_CREATED)


class ContentDeleteView(APIView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        id = data['id']
        try:
            Content.objects.filter(id=id).delete()
            ContentOptions.objects.filter(content=id).delete()
        except:
            pass

        return response.Response(data="Deleted", status=status.HTTP_200_OK)