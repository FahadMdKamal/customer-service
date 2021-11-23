from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group, User
from .serializers import GroupSerializer, UserSerializers, CoreTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CreateUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format='json'):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data)
        return Response(serializer.errors)

class GroupsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        # return Response(serializer.data)

        serializer = GroupSerializer(groups, many=True, context={"request": request})
        return Response(serializer.data)


class CoreTokenObtainPairView(TokenObtainPairView):
    serializer_class = CoreTokenObtainPairSerializer