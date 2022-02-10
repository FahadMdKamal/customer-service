from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.serializers import ModelSerializer
from .models import *
from django.core.exceptions import ValidationError
from .utils.static_dictionary import intent_terms_validated


class NluImportSerializer(serializers.Serializer):
    files = serializers.FileField()


class StaticDictionarySerializer(ModelSerializer):
    class Meta:
        model = StaticDictionary
        fields = ("id", "term_type", "term_context", "term_value", "order")

    def create(self, validated_data):
        if StaticDictionary.objects.filter(term_type=validated_data["term_type"].upper(),
                                           term_value=validated_data["term_value"].upper()).exists():
            raise serializers.ValidationError({"detail": "Item already exists in"})

        q = StaticDictionary(term_type=validated_data["term_type"].upper(),
                             term_context=validated_data["term_context"].upper(),
                             term_value=validated_data["term_value"].upper(),
                             order=validated_data["order"]
                             )
        q.save()
        return q


class ReversStaticDictionarySerializer(ModelSerializer):
    class Meta:
        model = StaticDictionary
        fields = ("id", "term_type", "term_context", "term_value", "order")


class ReversIntentSerializer(ModelSerializer):
    class Meta:
        model = NluIntent
        fields = ("id", "name", "short_code", "group", "marked", "nluutterances_set")
        depth = 1


class NluIntentSerializer(ModelSerializer):
    # group = StaticDictionarySerializer(read_only=True)
    intent_terms_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = NluIntent
        fields = ('id', 'name', 'short_code', 'intent_terms_id', 'marked')

    def create(self, validated_data):
        group_data = validated_data.pop("intent_terms_id")
        group = get_object_or_404(StaticDictionary, id=group_data)
        q = NluIntent(group=group, name=validated_data["name"], short_code=validated_data["short_code"],
                      marked=validated_data["marked"])
        q.save()
        return q


class NluEntitiesSerializer(ModelSerializer):
    class Meta:
        model = NluEntities
        fields = ('id', 'name', 'role', 'confidence_score', 'value', 'position')

    def create(self, validated_data):
        q = NluEntities(name=validated_data["name"],
                        role=validated_data["role"], 
                        confidence_score=validated_data["confidence_score"],
                        value=validated_data["value"], 
                        position=validated_data["position"])
        q.save()
        return q


class NluUtteranceSerializer(ModelSerializer):
    intent = NluIntentSerializer(read_only=True)
    intnt_id = serializers.IntegerField(write_only=True)
    id = serializers.IntegerField()

    class Meta:
        model = NluUtterances
        fields = (
            'id', 'name', 'intent', 'intnt_id', 'intent_confidence', 'sentence', 'entities', 'traits', 'comment',
            'status', 'trained',
            'weight')

    def create(self, validated_data):
        print(validated_data)
        id = validated_data.get('id', 0)

        print("ID------->", id)

        if id == 0:
            print("new entry")
            group_data = validated_data.pop("intnt_id")
            group = get_object_or_404(NluIntent, id=group_data)
            if validated_data["entities"]:
                for i in validated_data["entities"]:
                    try:
                        NluEntities.objects.get_or_create(name=i["name"],
                                                          role=i["role"], confidence_score=i["confidence_score"],
                                                          value=i["value"], position=[])
                    except:
                        pass

            if validated_data["traits"]:
                for i in validated_data["traits"]:
                    try:
                        StaticDictionary.objects.get_or_create(term_type=i["term_type"], term_context=i["term_context"],
                                                               term_value=i["term_value"], order=i["order"])
                    except:
                        pass

            q = NluUtterances(intent=group, name=validated_data["name"],
                              sentence=validated_data["sentence"], entities=validated_data["entities"],
                              traits=validated_data["traits"], comment=validated_data.get("comment", ""),
                              status=validated_data["status"],
                              weight=validated_data["weight"])
            q.save()
        else:
            q = get_object_or_404(NluUtterances, id=id)
            if validated_data["entities"]:
                for i in validated_data["entities"]:
                    try:
                        NluEntities.objects.get_or_create(name=i["name"],
                                                          role=i["role"], confidence_score=i["confidence_score"],
                                                          value=i["value"], position=[])
                    except:
                        pass

            if validated_data["traits"]:
                for i in validated_data["traits"]:
                    try:
                        StaticDictionary.objects.get_or_create(term_type=i["term_type"], term_context=i["term_context"],
                                                               term_value=i["term_value"], order=i["order"])
                    except:
                        pass

            q.entities = validated_data['entities']
            q.traits = validated_data['traits']
            q.status = validated_data['status']
            q.intent_id = validated_data['intnt_id']
            q.weight = validated_data['weight']
            q.save()
        return q

    def update(self, instance, validated_data):
        pass


class NluSyncViewSetSerializer(ModelSerializer):
    class Meta:
        model = NluSync
        fields = "__all__"


class NluUtterStatusSetSerializer(ModelSerializer):
    class Meta:
        model = NluSync
        fields = ("property_response", "status", "request_at", "completed_at", "created_at")


class NluImportDataSerializer(ModelSerializer):
    class Meta:
        model = NluImportFile
        fields = "__all__"
