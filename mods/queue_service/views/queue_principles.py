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
    def post(self,request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        if 'online' not in body or 'principle_id' not in body:
            return Response({'message':'Required field missing'},status=status.HTTP_400_BAD_REQUEST)
            
        if body['online']== 'agent_present':
            QueuePrinciples.objects.filter(principle_id=body['principle_id']).update(online='agent_present',last_active_at=datetime.now())
            return Response({'message':'Status updated successfully!'},status=status.HTTP_200_OK)
        if body['online']== 'agent_not_present':
            QueuePrinciples.objects.filter(principle_id=body['principle_id']).update(online='agent_not_present')
            return Response({'message':'Status updated successfully!'},status=status.HTTP_200_OK)

       
