from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.mavrik_apps.serializers import MavrikAppSerializer
from apps.mavrik_apps.models import MavrikApps
from apps.core.utils import decorate_response


class MavrikAppApiView(APIView):
    """
    Responsible for showing app list or filtering apps based on user query.
    :if the url contians {app-code} peramiter it will show the response either pass or fail
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
            groups = MavrikApps.objects.all()
            serializer = MavrikAppSerializer(groups, many=True)

            serializer = MavrikAppSerializer(groups, many=True, context={"request": request})
            return Response(serializer.data)
    

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
                return decorate_response(serializer.data, True, status.HTTP_201_CREATED, "App")
        else:
            serializer = MavrikAppSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return decorate_response(serializer.data, True, status.HTTP_201_CREATED, "App")
        return decorate_response(serializer.errors, True, status.HTTP_400_BAD_REQUEST, "App")
