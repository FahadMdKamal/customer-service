from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from apps.core.serializers import ChangePasswordSerializer
from django.contrib.auth.hashers import make_password
import json
from apps.core.serializers.password_reset_serializers import SetNewPasswordSerializer
from apps.core.utils import is_password_change_valid
        
class ChangePasswordView(APIView):
    """
    An endpoint for changing password.
    """

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = self.request.user
        serializer = ChangePasswordSerializer(data=request.data, user=request.user)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            user.set_password(serializer.validated_data["new_password"])
            if not is_password_change_valid(user, password=serializer.validated_data["new_password"]):
                return Response({'message': 'This password could not be used now'}, status=status.HTTP_200_OK)

            user.save()
            return Response({'message': 'Password changed successfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UpdateUserPassword(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                user = User.objects.get(pk=data['id'])
                serializer_data = SetNewPasswordSerializer(instance=user,data=data, partial=True)
                
                if serializer_data.is_valid():
                    user.password = make_password(data.get('password'))
                    if not is_password_change_valid(user, password=data.get('password')):
                        return Response({'message': 'This password could not be used now'}, status=status.HTTP_200_OK)

                    user.save()
                    return Response({'message': 'Password Changed Successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response(serializer_data.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
            except :
                return Response({'message': 'Sorry Faild to change Password'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'User Id is required'}, status=status.HTTP_400_BAD_REQUEST)
