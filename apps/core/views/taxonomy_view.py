from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView, status
from rest_framework.response import Response
from apps.core.models import Taxonomy
from apps.core.serializers import TaxonomySerilizer
import json


class TaxonomyCreateUpateView(APIView):

    def post(self, request, format='json'):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                flow = Taxonomy.objects.get(pk=data['id'])
                serializer = TaxonomySerilizer(flow, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                pass
        else:
            serializer = TaxonomySerilizer(data=request.data)
            if serializer.is_valid():
                flow = serializer.save()
                if flow:
                    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaxonomyListOrFilterView(APIView):

    def get(self, request):
        taxo_type = request.GET.get('type', None)
        if taxo_type:
            taxos = Taxonomy.objects.filter(taxonomy_type=taxo_type).order_by("-id")
        else:
            taxos = Taxonomy.objects.all().order_by("-id")
        taxonomies = TaxonomySerilizer(taxos, many=True)
        if taxonomies.data:
            return Response(taxonomies.data, status=status.HTTP_200_OK)
        return Response({"message": "No Taxonomies Found"}, status=status.HTTP_404_NOT_FOUND)


class TaxonomyDeleteView(APIView):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                obj = Taxonomy.objects.get(pk=data['id'])
                obj.delete()
                return Response(status=200, data={"message": "Taxonomy deleted successfully."})
            except ObjectDoesNotExist:
                return Response(status=404, data={"message": "Taxonomy not found."})
        else:
            return Response(status=404, data={"message": "Taxonomy not found."})
