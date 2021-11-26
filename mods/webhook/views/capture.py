from rest_framework.generics import CreateAPIView

from mods.webhook.serializers import CaptureSerializer
from mods.webhook.tasks import process_webhook


class CaptureView(CreateAPIView):
    serializer_class = CaptureSerializer

    def perform_create(self, serializer):
        webhook = serializer.save()
        process_webhook.delay(webhook.uuid)
        if webhook.topic == "something":
            # TODO Business logic for instant reply
            pass
