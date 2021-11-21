from rest_framework.viewsets import ModelViewSet

from mods.content.models import ContentData
from mods.content.serializers import ContentDataSerializer


class ContentDataView(ModelViewSet):
    serializer_class = ContentDataSerializer
    queryset = ContentData.objects.all().order_by('-id')