from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from apps.core.models.taxonomy import Taxonomy
from apps.core.serializers import TaxonomyListSerilizer
from mods.content.models import MessageTemplate
from mods.content.serializers import MessageTemplateSerializer
from rest_framework import response
from rest_framework import status
import json
from apps.core.utils import upload_handler

import markdown


class MessageTemplateCreateOrUpdateView(APIView):

    def post(self, request):
        if request.data.get('id') is not None and int(request.data.get('id')) > 0:
            try:
                message_template = MessageTemplate.objects.filter(pk=request.data.get('id')).first()
                if request.data.get('file', None):
                    request.data['attachment'] = upload_handler(request)
                    request.data.pop('file')
                serializer = MessageTemplateSerializer(message_template, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                pass
        else:
            if request.data.get('file', None):
                request.data['attachment'] = upload_handler(request)
                request.data.pop('file')
           
            serializer = MessageTemplateSerializer(data=request.data)
            if serializer.is_valid():
                
                message_template = serializer.save()
                if message_template:
                    return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageTemplateListView(APIView):

    def get(self, request, format=None):
        params = {}

        if self.request.query_params.get("template-group-id", None) is not None:
            params.update({"template_group_id": self.request.query_params["template-group-id"]})

        if self.request.query_params.get("app-id", None) is not None:
            params.update({"app_id": self.request.query_params["app-id"]})

        if self.request.query_params.get("channel-type", None) is not None:
            params.update({"allowed_channel_types": self.request.query_params["channel-type"]})

        data = []
        nextPage = 0
        previousPage = 0
        
        raw_page = request.GET.get('page')
        raw_limit = request.GET.get('limit')
        page = int(raw_page) if raw_page and raw_page.isdigit() else 1
        limit = int(raw_limit) if raw_limit and raw_limit.isdigit() else 10
        message_template = MessageTemplate.objects.filter(**params).order_by('-id')

        paginator = Paginator(message_template, limit)
        try:
            data = paginator.page(page)
        except ObjectDoesNotExist:
            data = paginator.page(page)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = MessageTemplateSerializer(data, context={'request': request}, many=True)

        taxonomies_serializer = TaxonomyListSerilizer(Taxonomy.objects.all(), many=True)

        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return response.Response(
                {'data': serializer.data if page <= paginator.num_pages else [],
                'groups':taxonomies_serializer.data,
                 'count': paginator.count,
                 'total_pages': paginator.num_pages,
                 'next': nextPage,
                 'prev': previousPage,
                 'limit': limit})


class MessageTemplateDeleteView(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None:
            try:
                for id in data['id']:
                    if int(id) > 0:
                        message_template = get_object_or_404(MessageTemplate, pk=id)
                        message_template.delete()
                return response.Response(status=200, data={"message": "Message Template deleted successfully."})
            except ObjectDoesNotExist:
                return response.Response(status=404, data={"message": "Message Template not found."})

        else:
            return response.Response(status=404, data={"message": "Message Template not found."})


class MessageTemplateDetailsView(APIView):

    def get(self, request):
        params = {}
        message_template_id = int(request.GET.get('id'))

        if self.request.query_params.get("id", None) is not None:
            params.update({"id": self.request.query_params["id"]})

        if self.request.query_params.get("app-id", None) is not None:
            params.update({"app_id": self.request.query_params["app-id"]})

        if self.request.query_params.get("template-code", None) is not None:
            params.update({"template_code": self.request.query_params["template-code"]})

        if self.request.query_params.get("channel-type", None) is not None:
            params.update({"allowed_channel_types": self.request.query_params["channel-type"]})

        if message_template_id is not None and message_template_id > 0:
            try:
                message_template = MessageTemplate.objects.filter(**params).order_by('-id').last()
                serializer = MessageTemplateSerializer(message_template)
                if not message_template:
                    return response.Response(status=404, data={ "message": "Message Template not found."})
                return response.Response(status=200, data=serializer.data)
            except ObjectDoesNotExist:
                return response.Response(status=404, data={ "error":serializer.errors, "message": "Message Template not found."})

        else:
            return response.Response(status=404, data={"message": "Message Template not found."})

