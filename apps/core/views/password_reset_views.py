from django.http.response import HttpResponsePermanentRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.hashers import make_password

from django.contrib.auth.tokens import PasswordResetTokenGenerator
import json, os
from django.urls import reverse
from rest_framework import status
from apps.core.utils import Util

from apps.core.serializers import SetNewPasswordSerializer
from apps.core.utils import is_password_change_valid


class CustomRedirect(HttpResponsePermanentRedirect):

    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']


class PasswordResetAPIView(APIView):
    
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))

        email = data.get('email', '')

        try:
            if email:
                user_obj = User.objects.get(email=email)
                if user_obj:
                    uidb64 = urlsafe_base64_encode(force_bytes(user_obj.pk))
                    token = PasswordResetTokenGenerator().make_token(user_obj)
                    current_site = get_current_site(request=request).domain

                    relativeLink = reverse('core:password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
                    absurl = 'http://'+current_site + relativeLink

                    email_body = 'Hello, \n Use link below to reset your password  \n' + absurl
                
                    data = {
                        'email_body': email_body, 
                        'to_email': user_obj.email,
                        'email_subject': 'Reset your passsword'
                        }
                    Util.send_email(data)
                return Response({'message':'Password Reset Link was sent', 'token': token, 'uidb64': uidb64}, status=status.HTTP_200_OK)
        except:
            return Response({'message':'Invalid email or No User found With the Given email'}, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmAPIView(APIView):
    
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            if user is not None and PasswordResetTokenGenerator().check_token(user,token):
                id = force_text(urlsafe_base64_decode(uidb64))
                user = User.objects.get(id=id)
                
                return Response({'message':'Please Enter Password', 
                    'token': token, 
                    'uidb64': uidb64 }, status=status.HTTP_200_OK)
            else:
                return Response({'message':'Token might be expired or invalid'}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({'message':'Password Reset Token is Invalid'}, status=status.HTTP_400_BAD_REQUEST)


class CompleteResetPassword(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))

        try:
            uidb64 = data.get('uidb64')
            token = data.get('token')
            uid = force_text(urlsafe_base64_decode(uidb64))

            user = User.objects.get(pk=uid)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'message': 'Invalid attempt, token or uid isn\'t valid.'}, status=status.HTTP_400_BAD_REQUEST)
                
            else:
                serializer_data = SetNewPasswordSerializer(instance=user,data=data)
                
                if serializer_data.is_valid():
                    user.password = make_password(data.get('password'))
                    if not is_password_change_valid(user, password=data.get('password')):
                        return Response({'message': 'This password could not be used now'}, status=status.HTTP_200_OK)

                    user.save()
                    return Response({'message': 'Password Changed Successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

        except :
            return Response({'message': 'Could not Change the Password'}, status=status.HTTP_400_BAD_REQUEST)
