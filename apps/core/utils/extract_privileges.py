from apps.core.models import WorkGroups, Apps, Channels
from apps.core.serializers.workgroup_serializers import WorkGroupListSerializers
from apps.core.serializers.channel_serializers import ChannelsListSerializer
from apps.core.serializers.app_serilizers import AppListSerializer


class UserPrivileges:

    def get_apps(self, user):
        """
        Returns user privileged Apps
        """
        return Apps.objects.filter(channel_app__channel_workgroup__user__id=user.id).distinct()

    def get_channels(self, user):
        """
        Returns user privileged Channels
        """
        return Channels.objects.filter(channel_workgroup__user__id=user.id).distinct()

    def get_workgroup(self, user):
        """
        Returns user privileged workgroups
        """
        return Channels.objects.filter(user__id=user.id).distinct()


def get_user_privileges(user):
    """
    Pass User Object to get Previleged Apps, Channels, Workgroups
    """
    # UserPrivileges().get_apps(user)
    workgroups = WorkGroups.objects.filter(user__id=user.id).select_related('channel')
    
    channel_set, workgroup_set, apps_set = set(), set(), set(),

    for wg in workgroups:
        workgroup_set.add(wg)
        channel_set.add(wg.channel)
        apps_set.add(wg.channel.app)

    return {
        "workgroups": WorkGroupListSerializers(workgroup_set, many=True).data, 
        "channels": ChannelsListSerializer(channel_set, many=True).data, 
        "apps": AppListSerializer(apps_set, many=True).data
        }
