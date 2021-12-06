from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from apps.core.serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
import json

from apps.core.serializers.password_reset_serializers import SetNewPasswordSerializer


class ChangePasswordView(APIView):
    """
    An endpoint for changing password.
    """

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        self.object = request.user
        serializer = ChangePasswordSerializer(data=data)
        if serializer.is_valid():
            print(serializer.data.get("old_password"))
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'message': 'Password updated successfully'
            }
            return Response(response, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserPassword(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                user = User.objects.get(pk=data['id'])
                serializer_data = SetNewPasswordSerializer(instance=user,data=data, partial=True)
                
                if serializer_data.is_valid():
                    user.password = make_password(data.get('password'))
                    user.save()
                    return Response({'message': 'Password Changed Successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response(serializer_data.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
            except :
                return Response({'message': 'Sorry Faild to change Password'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'User Id is required'}, status=status.HTTP_400_BAD_REQUEST)
