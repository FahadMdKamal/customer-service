from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action

from mods.nlu.models import NluEntities
from mods.nlu.serializers import NluEntitiesSerializer


class NluEntitiesViewSet(ModelViewSet):
    """
    Nlu Entities resource endpoints
    """
    serializer_class = NluEntitiesSerializer
    queryset = NluEntities.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.query_params.get("unique", None) is not None:
            if self.request.query_params.get("unique", None) == 'true':
                return NluEntities.objects.distinct()
        else:
            return NluEntities.objects.all()


