import json
from datetime import datetime
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from mods.queue_service.models import QueueItems
from django.http import Http404, JsonResponse
from urllib import parse
from mods.queue_service.models import QueuePrinciples
from mods.queue_service.serializers import QueueItemsSerializer
from django.db.models import Count
from mods.queue_service.serializers import QueueItemsSerializer


class QueueItemPublish(CreateModelMixin, GenericAPIView):

    serializer_class = QueueItemsSerializer

    def get_object(self, pk):

        try:
            return QueueItems.objects.get(pk=pk)
        except QueueItems.DoesNotExist:
            raise Http404

    def post(self, request, *args, **kwargs):
        assignee = QueuePrinciples.objects.all().order_by("last_assigned_at").first()
        request.data['principle_id'] = assignee.principle_id
        data = self.create(request, *args, **kwargs)
        QueuePrinciples.objects.filter(principle_id=assignee.principle_id).update(last_assigned_at=datetime.now())
        assignee.last_assigned_at = datetime.now()
        assignee.save()
        return data

    def patch(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        if 'id' not in body:
            return Response({'message': 'Required field missing'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            snippet = self.get_object(body['id'])
            serializer = QueueItemsSerializer(snippet, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QueueItemClaim(APIView):
    serializer_class = QueueItemsSerializer

    def get_object(self, pk, id):
        try:
            return QueueItems.objects.get(pk=pk, principle_id=id)
        except QueueItems.DoesNotExist:
            raise Http404

    def post(self, request):
        body_unicode = self.request.body.decode('utf-8')
        body = json.loads(body_unicode)
        if 'id' not in body or 'principle_id' not in body:
            return Response({'message': 'Required field missing'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = self.get_object(body['id'], body['principle_id'])

            count = QueueItems.objects.filter(
                principle_id=body['principle_id'], status='attended').count()
            print(count)
            if count <= 5 and data.status == 'pending':
                serializer = QueueItemsSerializer(
                    data, data={'status': 'attended'}, partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif count > 5:
                return Response({'message': 'Max assign limit reached!'}, status=status.HTTP_400_BAD_REQUEST)
            elif data.status == 'attended':
                return Response({'message': 'Item is already assigned!'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Somethinng happened,try again!'}, status=status.HTTP_400_BAD_REQUEST)

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
            return Response({'message': 'Required field missing'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            self.get_object(body['id'])
            remove_qi = QueueItems.objects.filter(id=body['id']).delete()
            return Response({'message': 'Queue item remove is successfull'}, status=status.HTTP_200_OK)


class QueueItemList(ListAPIView):

    serializer_class = QueueItemsSerializer

    def get_queryset(self):
        url = self.request.get_full_path()
        param = dict(parse.parse_qsl(parse.urlsplit(url).query))
        snippet = QueueItems.objects.filter(**param).all()
        snippet = QueueItemsSerializer(snippet, many=True).data
        return snippet

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        return response

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)
