from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from mods.content.models import Flow
from mods.content.serializers import FlowSerializer, FlowDetailsSerializer
from rest_framework import response
from rest_framework import status
import json, re


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

        return Flow.objects.filter(**params).order_by('-id')


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


class UserIPView(APIView):
    def get(self, request, *args, **kwargs):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip_address = x_forwarded_for.split(',')[0]
        else:
            ip_address = request.META.get('REMOTE_ADDR')

        pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        verify = pat.match(ip_address)
        if verify:
            ip = ip_address
        else:
            ip = "Not Found"
        browser = request.META['HTTP_USER_AGENT']
        return response.Response(status=status.HTTP_200_OK, data={"ip": ip, "browser": browser})
