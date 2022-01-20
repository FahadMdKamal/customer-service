import json
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from mods.queue_service.models.queue_topics import QueueTopics
from mods.queue_service.serializers import TopicCreateSerializer
from django.http import Http404, JsonResponse
from urllib import parse

class TopicCreate(CreateModelMixin, GenericAPIView):
    
    serializer_class = TopicCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TopicStatusUpdate(CreateModelMixin, GenericAPIView):
    serializer_class = TopicCreateSerializer

    def get_object(self, pk):

        try:
            return QueueTopics.objects.get(pk=pk)
        except QueueTopics.DoesNotExist:
            raise Http404

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        if 'status' and 'id' not in body:
            return Response({'message':'Required field missing'},status=status.HTTP_400_BAD_REQUEST)
        else:
            snippet = self.get_object(body['id'])
            serializer=TopicCreateSerializer(snippet, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TopicList(ListAPIView):
    serializer_class = TopicCreateSerializer
    def get_queryset(self):
        url = self.request.get_full_path()
        param = dict(parse.parse_qsl(parse.urlsplit(url).query))
        snippet = QueueTopics.objects.filter(**param).all()
        snippet = TopicCreateSerializer(snippet,many=True).data
        return snippet
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        return response

    def get(self, request, *args, **kwargs):
            return self.list(self,request, *args, **kwargs)

class TopicReset(APIView):
    serializer_class = TopicCreateSerializer
    def post(self, request):
        body_unicode = self.request.body.decode('utf-8')
        body = json.loads(body_unicode)
        if 'app_id' not in body:
            return Response({'message':'Required field missing'},status=status.HTTP_400_BAD_REQUEST)
        else:
            reset_qs = QueueTopics.objects.filter(app_id=body['app_id']).delete()
            return Response({'message':'Queue reset is successfull'},status=status.HTTP_200_OK)
