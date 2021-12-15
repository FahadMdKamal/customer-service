from django.utils.text import slugify


def get_permission(request, permission_group_name):

        all_groups = request.user.groups.all()
        group_names = [slugify(group.name) for group in all_groups]

        if permission_group_name in group_names:
            return True
        return False