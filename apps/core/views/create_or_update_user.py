from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from apps.core.serializers import UserSerializers, UserUpdateSerializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import json


class CreateOrUpdateUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format='json'):

        data = json.loads(request.body.decode('utf-8'))
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                db_object = User.objects.get(pk=data['id'])
                serializer = UserUpdateSerializers(db_object, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                pass
        else:
            if 'password' in data:
                request.data['password'] = make_password(request.data['password'])
            serializer = UserSerializers(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                if user:
                    return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            