from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage

from apps.mavrik_apps.serializers import MavrikAppSerializer
from apps.mavrik_apps.models import MavrikApps
from apps.core.utils import decorate_response


class MavrikAppApiView(APIView):
    """
    Responsible for showing app list or filtering apps based on user query.
    :if the url contians {app-code} peramiter it will show the response either pass or fail.
    Page pages with Next or previous page number through :page param.
    """

    def get(self, request):
        if request.GET.get('app-code'):
            app_code = request.GET.get('app-code')
            try:
                apps = MavrikApps.objects.get(app_code=app_code.upper())
                serializer = MavrikAppSerializer(apps)
                return Response(serializer.data)    
            except ObjectDoesNotExist:
                return Response({"message":"No App Found"},status=status.HTTP_404_NOT_FOUND)
        else:
            obj_list = MavrikApps.objects.all().order_by('-id')
            serializer = MavrikAppSerializer(obj_list, many=True)

            data = []
            nextPage = 1
            previousPage = 1
            page = request.GET.get('page', 1)
            limit = request.GET.get('limit', 10)
            paginator = Paginator(obj_list, limit)
            try:
                data = paginator.page(page)
            except ObjectDoesNotExist:
                data = paginator.page(paginator.num_pages)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)

            serializer = MavrikAppSerializer(data, context={'request': request}, many=True)


            if data.has_next():
                nextPage = data.next_page_number()
            if data.has_previous():
                previousPage = data.previous_page_number()

            return Response(
                    {'data': serializer.data,
                    'count': paginator.count,
                    'total_pages': paginator.num_pages,
                    'next': nextPage,
                    'prev': previousPage,
                    'limit': limit}, 
                    status=status.HTTP_200_OK)


class MavrikAppCreateOrUpdateApiView(APIView):
    """
    Responsible for Creating or Updating Mavrik Apps.
    :if request contains id it will update object
    :if no id, it will create New Object
    :Send Channel Id(s) into channels: field as comma seperated values,
    serializer will handle crate or update based on those
    """

    def post(self, request, *args, **kwargs):
        
        if request.data.get('id'):
            db_object = MavrikApps.objects.get(id=request.data.get('id'))
            serializer = MavrikAppSerializer(db_object, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return decorate_response(serializer.data, True, status.HTTP_201_CREATED, "App Updated successfully")
        else:
            serializer = MavrikAppSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return decorate_response(serializer.data, True, status.HTTP_201_CREATED, "App Updated successfully")
        return decorate_response(serializer.errors, True, status.HTTP_400_BAD_REQUEST, "App Update Faild")

class MevrikAppDeleteApiView(APIView):

    def get(self, request):
        params = {}

        if self.request.query_params.get("app-id", None) is not None:
            params.update({"id": self.request.query_params["app-id"]})
        print(request.query_params.get('app-id'))
        
        app = MavrikApps.objects.filter(id=request.query_params.get('app-id'))
        if app:
            app.delete()
            return decorate_response(serializer_data="No Content", status=True, status_code=status.HTTP_204_NO_CONTENT, message="App Deleted Successfully")

        return decorate_response(serializer_data="No App Found", status=False, status_code=status.HTTP_404_NOT_FOUND, message="App Deletion Faild")
