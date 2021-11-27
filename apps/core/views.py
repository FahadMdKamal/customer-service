from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group, User

from apps.core.models import Texonomy
from .serializers import GroupSerializer, TexonomySerilizer, UserSerializers
from .serializers import GroupSerializer, UserSerializers, CoreTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password


class CreateUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format='json'):
        request.data['password'] = make_password(request.data['password'])
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


class TexonomyView(APIView):

    def get(self, request ):
        params = {}
        if self.request.query_params.get("type", None) is not None:
            params.update({"texonomy_type": self.request.query_params["type"]})
        return Texonomy.objects.get_texonomies_by_type(**params)

    def post(self, request, format='json'):
        serializer = TexonomySerilizer(data=request.data)
        if serializer.is_valid():
            texo = serializer.save()
            if texo:
                return Response(serializer.data)
        return Response(serializer.errors)

class CoreTokenObtainPairView(TokenObtainPairView):
    serializer_class = CoreTokenObtainPairSerializer
