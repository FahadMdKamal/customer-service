from rest_framework import permissions
from .permission_extractor import get_permission


class IsAVAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return get_permission(request, "av-admin")


class IsAVSupervisor(permissions.BasePermission):

    def has_permission(self, request, view):
        return get_permission(request, "av-supervisor")


class IsAVAgent(permissions.BasePermission):

    def has_permission(self, request, view):
        return get_permission(request, "av-agent")


class IsAVTeamlead(permissions.BasePermission):

    def has_permission(self, request, view):
        return get_permission(request, "av-teamlead")
        