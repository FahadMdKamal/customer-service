from rest_framework.views import APIView
from apps.core.serializers import CoreTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class TexonomyByTypeView(APIView):
    def get(self, request):
        params = {}
        if self.request.query_params.get("type", None):
            pass


class CoreTokenObtainPairView(TokenObtainPairView):
    serializer_class = CoreTokenObtainPairSerializer
