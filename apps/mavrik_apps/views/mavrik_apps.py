from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.mavrik_apps.serializers import MavrikAppSerializer
from apps.mavrik_apps.models import MavrikApps


class MavrikAppApiView(APIView):
    serializer_class = MavrikAppSerializer

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
    
    def post(self, request):
        serializer = MavrikAppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  