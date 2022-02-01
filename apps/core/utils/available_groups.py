from apps.core.models import WorkGroups
from django.contrib.auth import get_user_model


def user_workgroup(user: get_user_model()) -> list:
    """
    return workgroups where user is available
    """
    # if not user.id:
    #     return []
    # return WorkGroups.objects.filter(user__id=user.id)
    return WorkGroups.objects.filter(user__id=user.id) if user.id else []


def workgroup_user(workgroup: WorkGroups) -> list:
    """
    return users of a particular workgroups
    """
    return [r for r in workgroup.user.all()]
