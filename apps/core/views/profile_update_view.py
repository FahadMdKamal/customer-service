from rest_framework import status
from rest_framework import views
from rest_framework.response import Response
from django.contrib.auth.models import User
from apps.core import serializers
from apps.core.serializers import UserProfileUpdateSerializers
from rest_framework.permissions import IsAuthenticated   

class ProfileUpdateView(views.APIView):
    """
    Endpoint for requested user's Profile Update
    """

    def get(self, request):
        return Response(UserProfileUpdateSerializers(request.user).data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = UserProfileUpdateSerializers(request.user, data=request.data, partial=True)

        if serializer.is_valid():
            user = serializer.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Profile updated successfully',
                'data': UserProfileUpdateSerializers(user).data
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        