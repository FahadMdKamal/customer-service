from django.db.models import F
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from mods.nlu.models import NluSync, NluUtterances
from mods.nlu.serializers import NluSyncViewSetSerializer
from mods.nlu.utils.entities import entity_get_or_create
from mods.nlu.utils.formatter import text_uppercase
from mods.nlu.utils.traits import traits_get_or_create
from mods.nlu.utils.utterances import utterance_entity_position, single_utterance_sync
from mods.nlu.utils.nlp import Nlp
from mevrik.settings import WIT_KEY

client = Nlp(access_token=WIT_KEY)


class NluSyncViewSet(viewsets.ViewSet):
    """

    """
    # authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        # intent sysn
        for i in NluSync.objects.get_all_intent():
            if NluSync.objects.single_intent_check(pk=i.id, owner_type="intent"):
                pass
            else:
                property_request = {"intent_name": i.name}
                NluSync.objects.create_nlusync(owner_id=i.id, owner_type="intent", property_request=property_request)

        # entity sync
        for e in NluSync.objects.get_all_entities():
            if NluSync.objects.single_intent_check(pk=e.id, owner_type="entities"):
                pass
            else:
                property_request = {"entity_name": e.name, "roles": [e.role]}
                NluSync.objects.create_nlusync(owner_id=e.id, owner_type="entities", property_request=property_request)
        # traits sync
        for t in NluSync.objects.get_all_traits():
            if NluSync.objects.single_intent_check(pk=t.id, owner_type="traits"):
                pass
            else:
                try:
                    property_request = {"name": t.term_context, "values": [t.term_value]}
                    NluSync.objects.create_nlusync(owner_id=e.id, owner_type="traits",
                                                   property_request=property_request)
                except:
                    pass
        # # Utteraces sync
        for u in NluSync.objects.get_all_utterances():
            data = u
            utterance = {}
            utterance.update({"text": data.name, "intent": text_uppercase(data.intent.name)})
            traits = []
            entities = []
            # entity data format like wit
            for d in data.entities:
                entity = d.get("name")
                if entity is not None:
                    position = utterance_entity_position(data.name, d["value"])
                    if d["role"]:
                        # print("role", d["role"])
                        entity = text_uppercase(d["name"]) + ":" + text_uppercase(d["role"])
                    else:
                        entity = text_uppercase(d["name"]) + ":" + text_uppercase(d["name"])
                    # # Entity Create or Get Entity
                    # entity_get_or_create(d["name"], d["role"])
                    entities.append({
                        "entity": entity,
                        "start": position["start"],
                        "end": position["end"],
                        "body": d["value"],
                        "entities": [],
                    })
            utterance.update({"entities": entities})

            # traits data format like wit
            for trit in data.traits:
                try:
                    trait_name = trit["term_context"]
                    trait_values = trit["term_value"]
                    traits.append({
                        "trait": trait_name,
                        "value": trait_values
                    })
                except:
                    pass

            utterance.update({"traits": traits})

            property_request = [utterance]

            if NluSync.objects.single_intent_check(pk=u.id, owner_type="utterances"):
                NluSync.objects.filter(owner_id=u.id, owner_type="utterances").update(property_request=property_request)
            else:
                NluSync.objects.create_nlusync(owner_id=u.id, owner_type="utterances",
                                               property_request=property_request)
                NluSync.objects.utterance_trained_status(u.id)
        # traits sync
        return Response({"Sync ..."}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        print("retrieve")
        # Single utterance sync with NluSync model
        data = ''
        for u in NluUtterances.objects.filter(pk=pk):
            data = u
            property_request = single_utterance_sync(data)

            if NluSync.objects.single_intent_check(pk=u.id, owner_type="utterances"):
                sync = NluSync.objects.get(owner_id=u.id, owner_type="utterances")
                sync.property_request = property_request
                sync.save()
                data = sync.__dict__
                NluUtterances.objects.filter(pk=u.id).update(status="trained", trained=F("trained") + 1)
            else:
                data = NluSync.objects.create_nlusync(owner_id=u.id, owner_type="utterances",
                                                      property_request=property_request)
                NluUtterances.objects.filter(pk=u.id).update(status="trained", trained=F("trained") + 1)
        serializer = NluSyncViewSetSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SyncIntent(viewsets.ViewSet):
    def list(self, request):
        intents = NluSync.objects.filter(owner_type="intent", status="pending")
        for n in intents:
            intent_name = n.property_request["intent_name"]

            data = intent_name.upper().strip().replace(' ', '_')
            try:
                resp = client.create_intent(intent_name=data)
            except:
                resp = client.intent_info(intent_name=data)
            try:
                NluSync.objects.filter(id=n.id, owner_type="intent").update(status="success", property_response=resp)
            except:
                pass
        return Response("Creating....", status=status.HTTP_200_OK)


class SyncEntities(viewsets.ViewSet):
    def list(self, request):
        intents = NluSync.objects.filter(owner_type="entities", status="pending")
        for n in intents:
            entity_name = n.property_request["entity_name"]
            roles = n.property_request["roles"]
            data = entity_name

            try:
                resp = client.create_entity(entity_name=data, roles=roles)
            except:
                pass
            try:
                resp = client.entity_info(entity_name=data)
            except:
                resp = ""
            try:
                NluSync.objects.filter(id=n.id, owner_type="entities").update(status="success", property_response=resp)
            except:
                pass

        return Response("Creating....", status=status.HTTP_200_OK)


class SyncTraits(viewsets.ViewSet):
    def list(self, request):
        traits = NluSync.objects.filter(owner_type="traits", status="pending")
        for n in traits:
            name = n.property_request["name"]
            values = n.property_request["values"]
            try:
                resp = client.create_trait(name=name, values=values)
            except:
                resp = client.trait_info(trait_name=name)
            try:
                NluSync.objects.filter(id=n.id, owner_type="traits").update(status="success", property_response=resp)
            except:
                pass
        return Response("Creating....", status=status.HTTP_200_OK)


class SyncUtterances(viewsets.ViewSet):
    def list(self, request):
        utterances = NluSync.objects.filter(owner_type="utterances")
        for u in utterances:
            property_request = u.property_request
            intent_name = property_request[0]["intent"]
            try:
                intent_create = client.create_intent(intent_name=intent_name)
            except:
                intent_create = ""
            # Entity list and get or create in WIT
            entiti_list = property_request[0]["entities"]
            for en in entiti_list:
                ent_name = en["entity"].split(":")[0]
                ent_role = en["entity"].split(":")[1]
                entity_get_or_create(name=ent_name, roles=[ent_role])

            # Traits list and get or create in WIT
            traits_list = property_request[0]["traits"]
            for tl in traits_list:
                traits_get_or_create(name=tl["trait"], val=tl["value"])

            try:
                utter = client.train(property_request)
            except:
                pass

            if utter:
                # Confidence Score update in Entities
                try:
                    NluSync.objects.filter(id=u.id, owner_type="utterances").update(status="trained",
                                                                                    property_response=utter)
                except:
                    pass
        return Response("Creating....", status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        print("retrieve :: ")
        utterances = NluSync.objects.filter(owner_type="utterances", owner_id=pk)
        for u in utterances:
            property_request = u.property_request
            intent_name = property_request[0]["intent"]
            try:
                intent_create = client.create_intent(intent_name=intent_name)
            except:
                intent_create = ""
            # Entity list and get or create in WIT
            entiti_list = property_request[0]["entities"]
            for en in entiti_list:
                ent_name = en["entity"].split(":")[0]
                ent_role = en["entity"].split(":")[1]
                entity_get_or_create(name=ent_name, roles=[ent_role])

            # Traits list and get or create in WIT
            traits_list = property_request[0]["traits"]
            for tl in traits_list:
                traits_get_or_create(name=tl["trait"], val=tl["value"])

            try:
                utter = client.train(property_request)
            except:
                utter = ""

            if utter:
                # Confidence Score update in Entities
                try:
                    # data = NluSync.objects.filter(id=u.id, owner_type="utterances").update(status="trained",
                    #                                                                 property_response=utter)
                    sync = NluSync.objects.get(id=u.id, owner_type="utterances")
                    sync.property_response = utter
                    sync.status = "trained"
                    sync.save()
                    data = sync.__dict__
                    serializer = NluSyncViewSetSerializer(data)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except:
                    pass

        return Response("Creating....single", status=status.HTTP_200_OK)
