from rest_framework import permissions
from .permission_extractor import get_permission


class IsEmailAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return get_permission(request, "email-admin")


class IsEmailSupervisor(permissions.BasePermission):

    def has_permission(self, request, view):
        return get_permission(request, "email-supervisor")


class IsEmailAgent(permissions.BasePermission):

    def has_permission(self, request, view):
        return get_permission(request, "email-agent")
