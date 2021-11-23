from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from mods.content.models import Flow
from mods.content.serializers import FlowSerializer
from rest_framework import response
from rest_framework import status
import json


class FlowCreateOrUpdateView(APIView):
    def get(self):
        pass

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                flow = Flow.objects.get(pk=data['id'])
                serialized_flow = FlowSerializer(data=flow)

                if serialized_flow.is_valid():
                    serialized_flow.create()

                return response.Response(data={'message': 'flow updated successfully', 'data': data},
                                         status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                pass

        else:
            serializer = FlowSerializer(data=request.data)
            if serializer.is_valid():
                flow = serializer.save()
                if flow:
                    return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlowListView(APIView):
    def get(self, request, format=None):
        transformers = Flow.objects.all().order_by('-id')
        serializer = FlowSerializer(transformers, many=True)
        return response.Response(serializer.data)


class FlowDeleteView(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                flow = Flow.objects.get(pk=data['id'])
                flow.delete()
                return response.Response(status=200, data={"Flow deleted successfully."})
            except ObjectDoesNotExist:
                return response.Response(status=404, data={"Flow not found."})

        else:
            return response.Response(status=404, data={"Flow not found."})
