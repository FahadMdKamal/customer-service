
from apps.core.models import WorkGroups
from apps.core.serializers.workgroup_serializers import WorkGroupListSerializers
from apps.core.serializers.channel_serializers import ChannelsListSerializer
from apps.core.serializers.app_serilizers import AppListSerializer

def get_user_privileges(user):
    """
    Pass User Object to get Previleged Apps, Channels, Workgroups
    """
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