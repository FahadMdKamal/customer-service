from rest_framework import permissions
from django.utils.text import slugify


class IsLivechatAdmin(permissions.BasePermission):

    def has_permission(self, request, view):

        all_groups = request.user.groups.all()
        group_names = [slugify(group.name) for group in all_groups]

        if "chatbot-admin" in group_names:
            return True
        return False


class IsLivechatAgent(permissions.BasePermission):

    def has_permission(self, request, view):

        all_groups = request.user.groups.all()
        group_names = [slugify(group.name) for group in all_groups]

        if "chatbot-agent"  in group_names:
            return True
        return False


class IsLivechatTeamlead(permissions.BasePermission):

    def has_permission(self, request, view):

        all_groups = request.user.groups.all()
        group_names = [slugify(group.name) for group in all_groups]

        if "chatbot-teamlead"  in group_names:
            return True
        return False
        