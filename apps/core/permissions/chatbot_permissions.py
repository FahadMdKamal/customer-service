from rest_framework import permissions
from .permission_extractor import get_permission


class IsChatBotAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return get_permission(request, "chatbot-admin")


class IsChatBotTrainer(permissions.BasePermission):

    def has_permission(self, request, view):
        return get_permission(request,  "chatbot-trainer")
