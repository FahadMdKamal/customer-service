from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .user_serializers import UserSerializers
from apps.core.models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


class CoreTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        user_profile = None
        # Get User with the username
        user_obj = User.objects.get(username= attrs.get('username'))
        
        if user_obj and not user_obj.is_staff:
            user_profile = user_obj.profile_data
            if user_obj.profile_data.login_attempts < 3:
                # If login attempts less than 3 than increase attempt else raise error
                user_profile.login_attempts +=1
                user_profile.save()
            else:
                raise ValidationError({"message": "Account locked because of invalid login attempts. Please contact an admin"})
        
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if refresh and user_profile:
            # If login success set attempt to Zero
            user_profile.login_attempts =0
            user_profile.save()

        # Add extra responses here
        data['user'] = UserSerializers(self.user).data
        return data
