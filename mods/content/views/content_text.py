from rest_framework.viewsets import ModelViewSet

from mods.content.models import ContentText
from mods.content.serializers import ContentTextSerializer


class ContentTextView(ModelViewSet):
    serializer_class = ContentTextSerializer
    queryset = ContentText.objects.all().order_by('-id')