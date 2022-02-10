from rest_framework.views import APIView, status
from rest_framework.response import Response
from apps.core.models import WorkGroups
from apps.core.serializers import WorkGroupSerializers, UserSerializers
from apps.core.utils.available_groups import users_in_workgroup, workgroups_of_user
from apps.core.serializers.workgroup_serializers import UserSerializers
from apps.core.utils.api_response_decorator import decorate_response


class WorkGroupCreateUpdateView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        if 'id' in data and data['id'] is not None and int(data['id']) > 0:
            try:
                work_group = WorkGroups.objects.get(pk=data['id'])
                serializer = WorkGroupSerializers(work_group, data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return decorate_response(True, status.HTTP_201_CREATED, "Workgroup updated successfully", serializer.data)
                else:
                    return decorate_response(False, status.HTTP_400_BAD_REQUEST, "Could not update Workgroup", serializer.errors)
            except WorkGroups.DoesNotExist:
                    return decorate_response(False, status.HTTP_400_BAD_REQUEST, "Could not update Workgroup", "Workgroup does not exists")
        else:
            serializer = WorkGroupSerializers(data=request.data)
            if serializer.is_valid():
                work_group = serializer.save()
                if work_group:
                    return decorate_response(True, status.HTTP_201_CREATED, "Workgroup Created", serializer.data)
            return decorate_response(False, status.HTTP_400_BAD_REQUEST, "Could not Create Workgroup", serializer.errors)

    def get(self, request):
        usr_role = request.GET.get('role', None)
        if usr_role:
            grps = WorkGroups.objects.filter(
                user_role=usr_role).order_by("-id")
        else:
            grps = WorkGroups.objects.all().order_by("-id")
        serializer = WorkGroupSerializers(grps, many=True)
        if serializer.data:
            return decorate_response(True, status.HTTP_200_OK, "Workgroup list", serializer.data)
        return decorate_response(False, status.HTTP_404_NOT_FOUND, "No Workgroup Found", [])


class UserWithWorkGroups(APIView):
    def get(self, request):

        params = {}

        if self.request.query_params.get("workgroup-id", None) is not None:
            params.update({"id": self.request.query_params["workgroup-id"]})
        work_group = WorkGroups.objects.filter(**params).first()

        _user_list = users_in_workgroup(request.user)
        workgroups = WorkGroupSerializers(_user_list, many=True)

        workgroup_user_list = workgroups_of_user(work_group)
        serializer = UserSerializers(workgroup_user_list, many=True)
        return Response({'workgroups': workgroups.data, "users": serializer.data}, status=status.HTTP_200_OK)
