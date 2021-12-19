from rest_framework.views import APIView
from apps.core.serializers import CoreTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
import re
from user_agents import parse
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from hashlib import sha256
from django.contrib.auth import get_user_model
from apps.core.models import LoggedInUserInfo

User = get_user_model()


class CoreTokenObtainPairView(TokenObtainPairView):
    serializer_class = CoreTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            if serializer.is_valid(raise_exception=True):
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                
                if x_forwarded_for:
                    ip_address = x_forwarded_for.split(',')[0]
                else:
                    ip_address = request.META.get('REMOTE_ADDR')

                pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
                verify = pat.match(ip_address)
                if verify:
                    ip = ip_address
                else:
                    ip = "Not Found"
                browser = request.META['HTTP_USER_AGENT']
                user_agent = parse(browser)
                
                brand = user_agent.device.brand
                model = user_agent.device.model
                device_type = user_agent.get_device()

                user_agent_deatils = user_agent.browser.family + user_agent.os.family + ip
                
                # hash_value = sha256( user_agent_deatils.encode("utf-8") ).hexdigest()
                hash_value = sha256( user_agent_deatils.encode("utf-32") ).hexdigest().upper()
                user_obj = User.objects.get(username=request.data.get('username'))

                log_info_obj = LoggedInUserInfo.objects.filter(user=user_obj).first()

                if log_info_obj:
                    log_info_obj.hash = hash_value
                    log_info_obj.os = user_agent.os.family
                    log_info_obj.browser = user_agent.browser.family
                    log_info_obj.ip = ip
                    log_info_obj.save()
                else:
                    LoggedInUserInfo.objects.create(
                        user=user_obj, 
                        os=user_agent.os.family, 
                        browser=user_agent.browser.family, 
                        ip=ip, hash=hash_value)
                
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)