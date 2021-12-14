from rest_framework import permissions
from django.utils.text import slugify


class IsSocialCareAdmin(permissions.BasePermission):

    def has_permission(self, request, view):

        all_groups = request.user.groups.all()
        group_names = [slugify(group.name) for group in all_groups]

        if "social-care-admin" in group_names:
            return True
        return False


class IsSocialCareAgent(permissions.BasePermission):

    def has_permission(self, request, view):

        all_groups = request.user.groups.all()
        group_names = [slugify(group.name) for group in all_groups]

        if "social-care-agent"  in group_names:
            return True
        return False


class IsSocialCareTeamlead(permissions.BasePermission):

    def has_permission(self, request, view):

        all_groups = request.user.groups.all()
        group_names = [slugify(group.name) for group in all_groups]

        if "social-care-teamlead"  in group_names:
            return True
        return False
        