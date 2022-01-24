from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView, status
from rest_framework.response import Response
from apps.core.models import Taxonomy
from apps.core.serializers import TaxonomySerilizer
from django.core.paginator import Paginator, EmptyPage
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

    def get(self, request):

        params = {}

        if self.request.query_params.get("type", None) is not None:
            params.update({"taxonomy_type": self.request.query_params["type"]})

        if self.request.query_params.get("app-id", None) is not None:
            params.update({"app_id": self.request.query_params["app-id"]})

        obj_list = Taxonomy.objects.filter(**params).order_by("-id")
        data = []
        nextPage = 0
        previousPage = 0
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 10)
        paginator = Paginator(obj_list, limit)
        try:
            data = paginator.page(page)
        except ObjectDoesNotExist:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = TaxonomySerilizer(data, context={'request': request}, many=True)


        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response(
                {
                 'count': paginator.count,
                 'total_pages': paginator.num_pages,
                 'next': nextPage,
                 'prev': previousPage,
                 'limit': limit,
                'data': serializer.data,
                 }, 
                 status=status.HTTP_200_OK)


        # taxo_type = request.GET.get('type', None)
        # if taxo_type:
        #     taxos = Taxonomy.objects.filter(taxonomy_type=taxo_type).order_by("-id")
        # else:
        #     taxos = Taxonomy.objects.all().order_by("-id")
        # taxonomies = TaxonomySerilizer(taxos, many=True)
        # if taxonomies.data:
        #     return Response(taxonomies.data, status=status.HTTP_200_OK)
        # return Response({"message": "No Taxonomies Found"}, status=status.HTTP_404_NOT_FOUND)


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
