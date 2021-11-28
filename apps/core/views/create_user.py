from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.core.serializers import UserSerializers
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