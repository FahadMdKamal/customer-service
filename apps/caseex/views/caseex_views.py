from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from apps.caseex.serializers import CaseMessageSerializer
from apps.caseex.models import CaseMessage


class CaseMessageAPIView(APIView):
    """
    An endpoint for CaseAudience.
    """

    def get(self, request, *args, **kwargs):
        # data = request.data

        
        case_messages = CaseMessage.objects.all()
        
        serializer = CaseMessageSerializer(case_messages)
        # if serializer.is_valid():
        #     serializer.save()
        return Response({'data': serializer.data},status=status.HTTP_200_OK)
        # else:
        #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





















  # user = serializer.validated_data['user']
            # user.set_password(serializer.validated_data["new_password"])
            # if not is_password_change_valid(user, password=serializer.validated_data["new_password"]):
            #     return Response({'message': 'This password could not be used now'}, status=status.HTTP_200_OK)

            # user.save()