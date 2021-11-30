from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage

from rest_framework.views import APIView
from mods.content.models import MessageTemplate
from mods.content.serializers import MessageTemplateSerializer
from rest_framework import response
from rest_framework import status
import json


class MessageTemplateCreateOrUpdateView(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                message_template = MessageTemplate.objects.get(pk=data['id'])
                serializer = MessageTemplateSerializer(message_template, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                pass
        else:
            serializer = MessageTemplateSerializer(data=request.data)
            if serializer.is_valid():
                message_template = serializer.save()
                if message_template:
                    return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageTemplateListView(APIView):

    def get(self, request, format=None):
        message_template = MessageTemplate.objects.all().order_by('-id')
        data = []
        nextPage = 1
        previousPage = 1
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 10)
        paginator = Paginator(message_template, limit)
        try:
            data = paginator.page(page)
        except ObjectDoesNotExist:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = MessageTemplateSerializer(data, context={'request': request}, many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return response.Response(
                {'data': serializer.data,
                 'count': paginator.count,
                 'total_pages': paginator.num_pages,
                 'next': nextPage,
                 'prev': previousPage,
                 'limit': limit})


class MessageTemplateDeleteView(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                message_template = MessageTemplate.objects.get(pk=data['id'])
                message_template.delete()
                return response.Response(status=200, data={"Message Template deleted successfully."})
            except ObjectDoesNotExist:
                return response.Response(status=404, data={"Message Template not found."})

        else:
            return response.Response(status=404, data={"Message Template not found."})


class MessageTemplateDetailsView(APIView):

    def get(self, request):
        message_template_id = int(request.GET.get('id'))

        if message_template_id is not None and message_template_id > 0:
            try:
                flow = MessageTemplate.objects.filter(pk=message_template_id)
                serializer = MessageTemplateSerializer(flow, many=True)
                return response.Response(status=200, data=serializer.data)
            except ObjectDoesNotExist:
                return response.Response(status=404, data={"Message Template not found."})

        else:
            return response.Response(status=404, data={"Message Template not found."})
