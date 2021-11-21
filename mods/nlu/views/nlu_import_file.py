import csv
import io
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action

from mods.nlu.models import NluImportFile
from mods.nlu.serializers import NluImportDataSerializer


class NluImportDataView(viewsets.ViewSet):
    # authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)

    def list(self, request):
        return Response({"data": "ok"})

    def create(self, request):
        data = ''
        file_obj = request.FILES['file']
        intent_id = request.POST.get("intent_id", "")
        # Read csv file InMemoryUploadedFile
        file = file_obj.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(file))
        for data in reader:
            if intent_id:
                NluImportFile.objects.get_or_create(utterances=data["intent"], intent_id=intent_id)
            else:
                NluImportFile.objects.get_or_create(utterances=data["intent"])
        return Response({"data": "successfully created"})


class UtteranceUploadData(ModelViewSet):
    serializer_class = NluImportDataSerializer
    queryset = NluImportFile.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    @action(methods=['post'], detail=True)
    def intent_utterances(self, request, pk=None):
        recent_users = NluImportFile.objects.filter(intent_id=pk)

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)