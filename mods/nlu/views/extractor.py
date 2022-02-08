from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from ..utils import functions

class ExtratorViewSet(ViewSet):

    def create(self, request):
        params = []
        try:
            for k, v in request.data.items():
                if k == "func":
                    continue
                params.append(v)
            extractor = functions.Extractors()
            func = getattr(extractor, request.data.get('func'))(*params)
            return Response({"result": func })
        except:
            return Response({"result": 'Invalid Try' }, status=400)
