from mevrik.settings import WIT_KEY
from mods.nlu.utils.nlp import Nlp

client = Nlp(access_token=WIT_KEY)


def intent_get_or_create(intent_name):
    data = client.intent_info(intent_name=intent_name)
    if data:
        resp = data
    else:
        resp = client.create_intent(intent_name=intent_name)
    return resp