from rest_framework import permissions
from .permission_extractor import get_permission


class IsLivechatAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return get_permission(request, "chatbot-admin")


class IsLivechatAgent(permissions.BasePermission):

    def has_permission(self, request, view):
        return get_permission(request, "chatbot-agent")


class IsLivechatTeamlead(permissions.BasePermission):

    def has_permission(self, request, view):
        return get_permission(request, "chatbot-teamlead")
        