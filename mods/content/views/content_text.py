import json
from django.core.exceptions import ObjectDoesNotExist
from django.db.migrations import serializer
from rest_framework.views import APIView
from rest_framework import response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

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