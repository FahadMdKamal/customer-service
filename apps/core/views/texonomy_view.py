from rest_framework.views import APIView
from rest_framework.response import Response
from apps.core.serializers import TexonomySerilizer

class TexonomyView(APIView):
    #
    # def get(self, request ):
    #     params = {}
    #     if self.request.query_params.get("type", None) is not None:
    #         params.update({"texonomy_type": self.request.query_params["type"]})
    #     return Texonomy.objects.get_texonomies_by_type(**params)

    def post(self, request, format='json'):
        serializer = TexonomySerilizer(data=request.data)
        if serializer.is_valid():
            texo = serializer.save()
            if texo:
                return Response(serializer.data)
        return Response(serializer.errors)


class TexonomyByTypeView(APIView):
    def get(self, request):
        params = {}
        if self.request.query_params.get("type", None):
            pass

