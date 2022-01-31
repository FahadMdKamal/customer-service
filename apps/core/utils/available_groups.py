from operator import contains
from apps.core.models import WorkGroups
from django.contrib.auth import get_user_model


def userAvailableGroup(user):
    lst = []
    work_group_list = WorkGroups.objects.all()
    for grp in work_group_list:
        if user in grp:
            lst.append(grp)

    return lst
# from django.contrib.auth import get_user_model
# from apps.core.utils.available_groups.py
# user = get_user_model().objects.all().first()
# userAvailableGroup(user)
