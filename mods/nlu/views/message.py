from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from mods.nlu.utils.message import message_response


class MessageView(viewsets.ViewSet):
    """
    Messages
    """
    # authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self, request):
        params = {}
        data = request.data.get('data')
        if data:
            params.update(message_response(data))
        else:
            params = "Enter a Utterance"
        return Response(params, status=status.HTTP_200_OK)
