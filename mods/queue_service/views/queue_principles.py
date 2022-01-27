from datetime import datetime
import json
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from mods.queue_service import serializers
from mods.queue_service.models import QueueItems
from django.http import Http404, JsonResponse
from mods.queue_service.models import QueuePrinciples
from mods.queue_service.serializers import QueuePrinciplesSerializer



class PrincipleCreate(CreateModelMixin, GenericAPIView):
    
    serializer_class = QueuePrinciplesSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PrincipleOnline(APIView):
    serializers = QueuePrinciplesSerializer

    def get_object(self, pk):
        try:
            return QueuePrinciples.objects.get(principle_id=pk)
        except QueuePrinciples.DoesNotExist:
            raise Http404

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        if 'online' not in body or 'principle_id' not in body:
            return Response({'message': 'Required field missing'}, status=status.HTTP_400_BAD_REQUEST)

        data = self.get_object(body['principle_id'])
        if body['online'] == 'agent_present':
            serializer = QueuePrinciplesSerializer(data,
                                                   data={'online': 'agent_present', 'last_active_at': datetime.now()},
                                                   partial=True)
        if body['online'] == 'agent_not_present':
            serializer = QueuePrinciplesSerializer(data, data={'online': 'agent_not_present'}, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
