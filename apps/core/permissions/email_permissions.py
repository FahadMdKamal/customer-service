from rest_framework import permissions
from django.utils.text import slugify


class IsEmailAdmin(permissions.BasePermission):

    def has_permission(self, request, view):

        all_groups = request.user.groups.all()
        group_names = [slugify(group.name) for group in all_groups]

        if "email-admin" in group_names:
            return True
        return False


class IsEmailSupervisor(permissions.BasePermission):

    def has_permission(self, request, view):

        all_groups = request.user.groups.all()
        group_names = [slugify(group.name) for group in all_groups]

        if "email-supervisor"  in group_names:
            return True
        return False


class IsEmailAgent(permissions.BasePermission):

    def has_permission(self, request, view):

        all_groups = request.user.groups.all()
        group_names = [slugify(group.name) for group in all_groups]

        if "email-agent"  in group_names:
            return True
        return False
        