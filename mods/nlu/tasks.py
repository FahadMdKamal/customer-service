import time

from celery import shared_task
from celery.utils.log import get_task_logger
from .models import NluSync
from mevrik.settings import WIT_KEY
from mods.nlu.utils.nlp import Nlp

client = Nlp(access_token=WIT_KEY)
logger = get_task_logger(__name__)


@shared_task
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True


@shared_task()
def intent_sync_wit():
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

    return True


@shared_task
def entities_sync_wit():
    intents = NluSync.objects.filter(owner_type="entities", status="pending")
    for n in intents:
        entity_name = n.property_request["entity_name"]
        roles = n.property_request["roles"]
        data = entity_name
        try:
            resp = client.create_entity(entity_name=data, roles=roles)
        except:
            resp = client.entity_info(entity_name=data)
        try:
            NluSync.objects.filter(id=n.id, owner_type="entities").update(status="success", property_response=resp)
        except:
            pass
    return True

@shared_task
def traits_sync_wit():
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
    return True


@shared_task
def utterances_sync_wit():
    utterances = NluSync.objects.filter(owner_type="utterances", status="pending")[:10]
    for u in utterances:
        property_request = u.property_request
        intent_name = property_request[0]["intent"]
        try:
            intent_create = client.create_intent(intent_name=intent_name)
        except:
            intent_create = ""

        entiti_list = property_request[0]["entities"]
        for en in entiti_list:
            try:
                entity_create = client.create_entity(entity_name=en["entity"], roles=[])
            except:
                entity_create = ""
        try:
            utter = client.train(property_request)
        except:
            utter = ""
        if utter:
            try:
                NluSync.objects.filter(id=u.id, owner_type="utterances").update(status="success",
                                                                                property_response=utter)
            except:
                pass
    return True
