from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from mods.content.models import Content
from mods.content.serializers import ContentSerializer, ContentCreateSerializer
from rest_framework.views import APIView
from rest_framework import status


class ContentView(ModelViewSet):
    serializer_class = ContentSerializer
    queryset = Content.objects.all().order_by('-id')
    permission_classes = [IsAuthenticated]


class ContentCreateView(APIView):

    def post(self, request, format=None):
        serializer = ContentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
