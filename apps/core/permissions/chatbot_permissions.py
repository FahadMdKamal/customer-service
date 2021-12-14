from rest_framework import permissions
from django.utils.text import slugify


class IsChatBotAdmin(permissions.BasePermission):

    def has_permission(self, request, view):

        all_groups = request.user.groups.all()
        group_names = [slugify(group.name) for group in all_groups]

        if "chatbot-admin" in group_names:
            return True
        return False


class IsChatBotTrainer(permissions.BasePermission):

    def has_permission(self, request, view):

        all_groups = request.user.groups.all()
        group_names = [slugify(group.name) for group in all_groups]

        if "chatbot-trainer"  in group_names:
            return True
        return False
