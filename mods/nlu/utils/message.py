from mevrik.settings import WIT_KEY
from mods.nlu.utils.nlp import Nlp

client = Nlp(access_token=WIT_KEY)


def message_response(data):
    """
    Get the response from WIT and data process
    """
    params = {}
    resp = client.message(data)
    # Entities Reformate
    entities = []
    entities_key = []
    for i in resp["entities"].keys():
        entities_key.append(i)
    for k in entities_key:
        for y in resp["entities"][k]:
            entities.append(y)

    # Traits Reformate
    traits_key = []
    traits = []
    for i in resp["traits"].keys():
        traits_key.append(i)
    for tk in traits_key:
        try:
            data = resp["traits"][tk][0]
            traits.append(data)
        except:
            pass

    try:
        # if intent is PROFANITY_FILTER then entities and traits will be empty
        if resp["intents"][0]["name"] == "PROFANITY_FILTER":
            params.update({"utterances": resp["text"], "intents": resp["intents"], "entities": [],
                           "traits": []})
            return params
    except:
        pass

    if resp["intents"]:
        params.update({"utterances": resp["text"], "intents": resp["intents"], "entities": entities,
                       "traits": traits})
    else:
        # if intent not get then entities and traits will be empty
        params.update({"utterances": resp["text"], "intents": resp["intents"], "entities": [],
                       "traits": []})
    return params
