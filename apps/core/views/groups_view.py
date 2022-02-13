from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group
from apps.core.serializers import GroupSerializer

from apps.core.utils.api_response_decorator import decorate_response


class GroupsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)

        serializer = GroupSerializer(groups, many=True, context={"request": request})
        return decorate_response(status=True, status_code=status.HTTP_200_OK, message="User Permission Group(s)", serializer_data=serializer.data)
  