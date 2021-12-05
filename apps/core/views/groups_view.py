from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from apps.core.serializers import GroupSerializer

from django.contrib.auth.models import Group
from apps.core.models import App


class GroupsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.GET.get('app-slug'):
            try:
                app = App.objects.get(slug=request.GET.get('app-slug'))
                groups = app.groups.all()
                serializer = GroupSerializer(groups, many=True)
                return Response(serializer.data)    
            except ObjectDoesNotExist:
                return Response({"message":"No App Found"},status=status.HTTP_404_NOT_FOUND)
        else:
            groups = Group.objects.all()
            serializer = GroupSerializer(groups, many=True)

            serializer = GroupSerializer(groups, many=True, context={"request": request})
            return Response(serializer.data)
  
