import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from mods.queue_service.models import QueueItems
from django.http import Http404
from mods.queue_service.serializers import QueueItemsSerializer

class QueueItemPublish(CreateModelMixin, GenericAPIView):
    
    serializer_class = QueueItemsSerializer

    def get_object(self, pk):

        try:
            return QueueItems.objects.get(pk=pk)
        except QueueItems.DoesNotExist:
            raise Http404

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        if 'id' not in body:
            return Response({'message':'Required field missing'},status=status.HTTP_400_BAD_REQUEST)
        else:
            snippet = self.get_object(body['id'])
            serializer=QueueItemsSerializer(snippet, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QueueItemRemove(APIView):
    serializer_class = QueueItemsSerializer

    def get_object(self, pk):
        try:
            return QueueItems.objects.get(pk=pk)
        except QueueItems.DoesNotExist:
            raise Http404

    def post(self, request):
        body_unicode = self.request.body.decode('utf-8')
        body = json.loads(body_unicode)
        if 'id' not in body:
            return Response({'message':'Required field missing'},status=status.HTTP_400_BAD_REQUEST)
        else:
            self.get_object(body['id'])
            remove_qi = QueueItems.objects.filter(id=body['id']).delete()
            return Response({'message':'Queue item remove is successfull'},status=status.HTTP_200_OK)


class QueueItemList(APIView):

    serializer_class = QueueItemsSerializer

    def get(self, request, *args, **kwargs):
        params = {}

        if self.request.query_params.get("app-id", None) is not None:
            params.update({"id": self.request.query_params["app-id"]})

        qitms = QueueItems.objects.filter(**params).all()
        qitm_sr = QueueItemsSerializer(qitms, many=True).data
        return Response({'msg': qitm_sr})

    # def get_queryset(self):
    #     url = self.request.get_full_path()
    #     param = dict(parse.parse_qsl(parse.urlsplit(url).query))
    #     snippet = QueueItems.objects.filter(**param).all()
    #     snippet = QueueItemsSerializer(snippet,many=True).data
    #     return snippet
    
    # def list(self, request, *args, **kwargs):
    #     response = super().list(request, args, kwargs)
    #     return response

    # def get(self, request, *args, **kwargs):
    #     return self.list(self,request, *args, **kwargs)



