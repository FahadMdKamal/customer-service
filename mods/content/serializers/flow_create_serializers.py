from rest_framework import serializers


class FlowCreateSerializer(serializers.Serializer):
    name = serializers.Serializer()

