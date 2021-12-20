from rest_framework import permissions
from .permission_extractor import get_permission


class IsSocialCareAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return get_permission(request, "social-care-admin")


class IsSocialCareAgent(permissions.BasePermission):

    def has_permission(self, request, view):
        return get_permission(request, "social-care-agent")


class IsSocialCareTeamlead(permissions.BasePermission):

    def has_permission(self, request, view):
        return get_permission(request, "social-care-teamlead")

        