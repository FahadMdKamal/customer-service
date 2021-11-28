from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView, status
from rest_framework.response import Response
from apps.core.models import Texonomy
from apps.core.serializers import TexonomySerilizer
import json


class TexonomyCreateUpateView(APIView):

    def post(self, request, format='json'):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                flow = Texonomy.objects.get(pk=data['id'])
                serializer = TexonomySerilizer(flow, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                pass
        else:
            serializer = TexonomySerilizer(data=request.data)
            if serializer.is_valid():
                flow = serializer.save()
                if flow:
                    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TexonomyListOrFilterView(APIView):

    def get(self, request, texo_type=None):
        if texo_type:
            texos = Texonomy.objects.filter(texonomy_type=texo_type).order_by("-id")
        else:
            texos = Texonomy.objects.all().order_by("-id")

        texonomies = TexonomySerilizer(texos, many=True)
        if len(texonomies.data)>0:
            return Response(texonomies.data, status=status.HTTP_200_OK)
        return Response({"message": "No Texonomies Found"}, status=status.HTTP_404_NOT_FOUND)


class TexonomyDeleteView(APIView):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                obj = Texonomy.objects.get(pk=data['id'])
                obj.delete()
                return Response(status=200, data={"Texonomy deleted successfully."})
            except ObjectDoesNotExist:
                return Response(status=404, data={"Texonomy not found."})
        else:
            return Response(status=404, data={"Texonomy not found."})
