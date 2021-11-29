import json
from django.core.exceptions import ObjectDoesNotExist
from django.db.migrations import serializer
from rest_framework.views import APIView
from rest_framework import response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.contrib.postgres.search import SearchVector
from django.db.models import TextField
from django.db.models.functions import Cast
from mods.content.models import ContentText
from mods.content.serializers import ContentTextSerializer


class ContentTextModelView(ModelViewSet):
    serializer_class = ContentTextSerializer
    queryset = ContentText.objects.all()


class ContentTextView(APIView):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                flow = ContentText.objects.get(pk=data['id'])
                serializer = ContentTextSerializer(flow, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                pass
        else:
            serializer = ContentTextSerializer(data=request.data)
            if serializer.is_valid():
                flow = serializer.save()
                if flow:
                    return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContentTextSearchView(APIView):
    def post(self, request):
        search_data = request.data["data"]
        data = ContentText.objects.annotate(search=SearchVector(Cast('text_body', TextField())),).filter(search=search_data)
        if data:
            content_text = ContentText.objects.filter(pk=data.first().id)
            serializer = ContentTextSerializer(content_text, many=True)
            return response.Response(serializer.data)
        else:
            return response.Response(data="Not match", status=status.HTTP_400_BAD_REQUEST)