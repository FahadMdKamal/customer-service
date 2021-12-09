from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from mods.content.models import Flow, NodeConfig
from mods.content.serializers import FlowSerializer, FlowDetailsSerializer, IdSerializer, FlowIntentNodeSerializer
from rest_framework import response
from rest_framework import status
import json

from mods.nlu.models import NluIntent


class FlowCreateOrUpdateView(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                flow = Flow.objects.get(pk=data['id'])
                serializer = FlowSerializer(flow, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                pass
        else:
            serializer = FlowSerializer(data=request.data)
            if serializer.is_valid():
                flow = serializer.save()
                if flow:
                    return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlowListView(ModelViewSet):
    serializer_class = FlowSerializer
    queryset = Flow.objects.all().order_by('-id')
    http_method_names = ['get']

    def get_queryset(self):
        params = {}

        if self.request.query_params.get("app_id", None) is not None:
            params.update({"app_id": self.request.query_params["app_id"]})

        if self.request.query_params.get("group_id", None) is not None:
            params.update({"group_id": self.request.query_params["group_id"]})

        return Flow.objects.filter(**params).order_by('-id')


class FlowDeleteView(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        serializer = IdSerializer(data=request.data)
        if serializer.is_valid():
            if 'id' in data and data['id'] is not None and int(data['id']) > 0:
                try:
                    flow = Flow.objects.get(pk=data['id'])
                    flow.delete()
                    return response.Response(status=200, data={"Flow deleted successfully."})
                except ObjectDoesNotExist:
                    return response.Response(status=404, data={"Flow not found."})
            else:
                return response.Response(status=404, data={"Flow not found."})
        else:
            return response.Response(status=404, data=serializer.errors)


class FlowDetailsView(APIView):

    def get(self, request):
        flow_id = int(request.GET.get('id'))

        if flow_id is not None and flow_id > 0:
            try:
                flow = Flow.objects.filter(pk=flow_id)
                serializer = FlowDetailsSerializer(flow, many=True)
                return response.Response(status=200, data=serializer.data)
            except ObjectDoesNotExist:
                return response.Response(status=404, data={"Flow not found."})

        else:
            return response.Response(status=404, data={"Flow not found."})


class FlowIntent(APIView):
    def post(self, request, *args, **kwargs):
        errors = []
        intent_name = request.data.get("intent")
        try:
            data = NluIntent.objects.filter(name__icontains=intent_name).first()
        except:
            errors.append("not found intent")
        try:
            data = NodeConfig.objects.filter(value=data.id).first()
            flow_id = data.flow_node.flow.pk
        except:
            errors.append("not found")

        if len(errors) > 0:
            raise ValidationError(errors)

        if data:
            content_text = Flow.objects.filter(pk=flow_id)
            serializer = FlowIntentNodeSerializer(content_text, many=True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return response.Response(data="Not match", status=status.HTTP_202_ACCEPTED)
