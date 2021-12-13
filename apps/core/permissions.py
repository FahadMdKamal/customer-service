from rest_framework import permissions, views
from django.contrib.auth.models import User, Group

from rest_framework_simplejwt.authentication import JWTAuthentication


class IsEmailAdmin(permissions.BasePermission):


    def has_permission(self, request, view):
        JWT_authenticator = JWTAuthentication()
        response = JWT_authenticator.authenticate(request)
            
        if response is not None:
            user , token = response
            raw_groups = [name for name in token.payload.get('groups')]
            groups = [grp['name'] for grp in raw_groups]
            
            if "email-admin" in groups or request.user.is_staff:
                return True

        return False
        


# class IsEmailAdmin(permissions.BasePermission):

#     def has_permission(self, request, view):
#         user = request.user
#         safe_method = ['GET', 'PATCH']
#         groups = user.groups.all()
#         print(groups)
        # group_permission = user.get_group_permissions()
        # print(group_permission)

        # for group in groups:
        #     if group.name == "Live Chat AGENT":
        #         print('Yes')

        # return super().has_permission(request, view)