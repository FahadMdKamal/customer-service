from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

class TopicCreate(APIView):
    def get(self, request):
        return Response({'done':"Done"})