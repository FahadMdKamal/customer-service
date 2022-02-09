from apps.core.models import WorkGroups, Apps, Channels
from apps.core.serializers.workgroup_serializers import WorkGroupListSerializers
from apps.core.serializers.channel_serializers import ChannelsListSerializer
from apps.core.serializers.app_serilizers import AppListSerializer


class UserPrivileges:

    def __init__(self, user_instance):
        self.user = user_instance

    def get_apps(self) -> list[Apps]:
        """
        Returns user privileged Apps
        """
        return Apps.objects.filter(channel_app__channel_workgroup__user__id=self.user.id).distinct()

    def get_channels(self) -> list[Channels]:
        """
        Returns user privileged Channels
        """
        return Channels.objects.filter(channel_workgroup__user__id=self.user.id).distinct()

    def get_workgroup(self) -> list[WorkGroups]:
        """
        Returns user privileged workgroups
        """
        return WorkGroups.objects.filter(user__id=self.user.id).distinct()

    def get_serialized_user_privileges(self):
        """
        Pass User Object to get Previleged Apps, Channels, Workgroups
        """
        
        apps_set = self.get_apps()
        channel_set = self.get_channels()
        workgroup_set = self.get_workgroup()

        return {
            "apps": AppListSerializer(apps_set, many=True).data,
            "channels": ChannelsListSerializer(channel_set, many=True).data, 
            "workgroups": WorkGroupListSerializers(workgroup_set, many=True).data, 
            }
