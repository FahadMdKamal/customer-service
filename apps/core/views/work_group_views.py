from rest_framework.views import APIView, status
from rest_framework.response import Response
from apps.core.models import WorkGroups
from apps.core.serializers import WorkGroupSerializers
from django.core.exceptions import ObjectDoesNotExist
import json


class WorkGroupCreateUpdateView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                work_group = WorkGroups.objects.get(pk=data['id'])
                serializer = WorkGroupSerializers(work_group, data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                pass
        else:
            serializer = WorkGroupSerializers(data=request.data)
            if serializer.is_valid():
                work_group = serializer.save()
                if work_group:
                    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        usr_role = request.GET.get('role', None)
        if usr_role:
            grps = WorkGroups.objects.filter(
                user_role=usr_role).order_by("-id")
        else:
            grps = WorkGroups.objects.all().order_by("-id")
        workgroups = WorkGroupSerializers(grps, many=True)
        if workgroups.data:
            return Response(workgroups.data, status=status.HTTP_200_OK)
        return Response({"message": "No Workgroup Found"}, status=status.HTTP_404_NOT_FOUND)


class UserWithWorkGroups(APIView):
    def get(self, request):
        user_list = request.GET.get('user_workgroups')
        if user_list:
            obj_list = WorkGroups.objects.filter(
                user=user_list).order_by("-id")
        else:
            obj_list = WorkGroups.objects.all().order_by("-id")

        usr_list = WorkGroupSerializers(obj_list, many=True)
        if usr_list.data:
            return Response(usr_list.data, status=status.HTTP_200_OK)
