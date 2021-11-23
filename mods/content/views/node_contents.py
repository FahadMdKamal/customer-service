from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework import response, status
import json

from mods.content.models.node_contents import NodeContent
from mods.content.serializers import NodeContentSerializer


class AttachContentView(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        serializer = NodeContentSerializer(data=data)
        if serializer.is_valid():
            node_config = serializer.save()
            if node_config:
                return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteContentView(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                flow = NodeContent.objects.get(pk=data['id'])
                flow.delete()
                return response.Response(status=status.HTTP_204_NO_CONTENT, data={"Node-Content deleted successfully."})
            except ObjectDoesNotExist:
                return response.Response(status=status.HTTP_404_NOT_FOUND, data={"Node-Content not found."})

        else:
            return response.Response(status=status.HTTP_404_NOT_FOUND, data={"Node-Content not found."})
