from rest_framework import permissions
from django.utils.text import slugify


class IsAVAdmin(permissions.BasePermission):

    def has_permission(self, request, view):

        all_groups = request.user.groups.all()
        group_names = [slugify(group.name) for group in all_groups]

        if "av-admin" in group_names:
            return True
        return False


class IsAVSupervisor(permissions.BasePermission):

    def has_permission(self, request, view):

        all_groups = request.user.groups.all()
        group_names = [slugify(group.name) for group in all_groups]

        if "av-supervisor"  in group_names:
            return True
        return False


class IsAVAgent(permissions.BasePermission):

    def has_permission(self, request, view):

        all_groups = request.user.groups.all()
        group_names = [slugify(group.name) for group in all_groups]

        if "av-agent"  in group_names:
            return True
        return False


class IsAVTeamlead(permissions.BasePermission):

    def has_permission(self, request, view):

        all_groups = request.user.groups.all()
        group_names = [slugify(group.name) for group in all_groups]

        if "av-teamlead"  in group_names:
            return True
        return False
        