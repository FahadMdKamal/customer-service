from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
# from rest_framework_simplejwt.authentication import JWTAuthentication

from mods.nlu.models import NluIntent
from mods.nlu.serializers import NluIntentSerializer


class NluIntentViewSet(ModelViewSet):
    """
    Nlu Intent resource endpoints
    """
    serializer_class = NluIntentSerializer
    queryset = NluIntent.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    # permission_classes = [IsAuthenticated]


class NluIntentGroupViewSet(ModelViewSet):
    """
    Look Up resource endpoints
    """
    serializer_class = NluIntentSerializer
    queryset = NluIntent.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return NluIntent.objects.filter(group=self.request.query_params["id"])