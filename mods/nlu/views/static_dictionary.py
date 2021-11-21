from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
# from rest_framework_simplejwt.authentication import JWTAuthentication

from mods.nlu.models import StaticDictionary
from mods.nlu.serializers import ReversStaticDictionarySerializer, StaticDictionarySerializer


class StaticDictionaryViewSet(ModelViewSet):
    """
    Static Dictionary resource endpoints
    """
    serializer_class = StaticDictionarySerializer
    queryset = StaticDictionary.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    # permission_classes = [IsAuthenticated]


class NluLookupViewSet(ModelViewSet):
    """
    Look Up resource endpoints
    """
    serializer_class = ReversStaticDictionarySerializer
    queryset = StaticDictionary.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        params = {}
        if self.request.query_params.get("name", None) is not None:
            params.update({"term_type__icontains": self.request.query_params["name"]})

        if self.request.query_params.get("context", None) is not None:
            params.update({"term_context__icontains": self.request.query_params["context"]})
        return StaticDictionary.objects.filter(**params)