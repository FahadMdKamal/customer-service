from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from mods.nlu.utils.nlp import Nlp
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from mods.nlu.serializers import *
from mods.nlu.models import *
from mevrik.settings import WIT_KEY

client = Nlp(access_token=WIT_KEY)


class RetrainView(ModelViewSet):
    serializer_class = NluUtteranceSerializer
    queryset = NluUtterances.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        params = {}
        if self.request.query_params.get("intent_id", None) is not None:
            params.update({"intent_id": self.request.query_params["intent_id"]})

        if self.request.query_params.get("status", None) is not None:
            params.update({"status": self.request.query_params["status"]})

        if self.request.query_params.get("start", None) is not None and self.request.query_params.get("end", None):
            params.update(
                {"intent_confidence__range": (self.request.query_params["start"], self.request.query_params["end"])})

        if self.request.query_params.get("search", None) is not None:
            params.update({"sentence__search": self.request.query_params["search"]})

        return NluUtterances.objects.filter(**params).order_by('-id')


class NluUtterancesConfidenceView(viewsets.ViewSet):
    """
    User input data send to wit and get intent
    """
    # authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        resp = "OK"
        return Response(resp, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        intent_confidence_score = ""

        # get existing utterance text
        queryset = NluUtterances.objects.filter(id=pk).values("sentence", "id").first()
        try:
            resp = client.message(queryset["sentence"])
        except:
            resp = ""
        if resp:
            try:
                intent_confidence_score = resp.get("intents")[0]["confidence"]
            except IndexError:
                intent_confidence_score = 0
        # send to with to see the confidence scores
        # Update the confidence scores in NluUtterances table
        NluUtterances.objects.filter(id=pk).update(intent_confidence=float(intent_confidence_score))
        # NluUtterances.objects.filter(id=pk).update(intent_confidence=intent_confidence_score)
        resp = "successfully update the scores"
        return Response(resp, status=status.HTTP_200_OK)


class NluUtterancesFullTextSearchView(ModelViewSet):
    serializer_class = NluUtteranceSerializer
    queryset = NluUtterances.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        params = {}
        if self.request.query_params.get("text", None) is not None:
            params.update({"sentence__search": self.request.query_params["text"]})

        return NluUtterances.objects.filter(**params)