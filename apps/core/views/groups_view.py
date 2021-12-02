from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group, User

from apps.core.serializers import GroupSerializer


class GroupsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        # return Response(serializer.data)

        serializer = GroupSerializer(groups, many=True, context={"request": request})
        return Response(serializer.data)
