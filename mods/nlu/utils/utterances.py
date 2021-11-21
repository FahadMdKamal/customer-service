from mods.nlu.utils.formatter import text_uppercase


def utterance_entity_position(utterance, keyword):
    start = utterance.find(keyword)
    end = len(keyword) + start
    return {"start": start, "end": end}


def single_utterance_sync(data):
    buildin_entities = ["datetime", "email", "number", "phone_number"]
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
                entity = text_uppercase(d["name"]) + ":" + text_uppercase(d["role"])
            else:
                entity = text_uppercase(d["name"]) + ":" + text_uppercase(d["name"])
            entities.append({
                "entity": entity,
                "start": position["start"],
                "end": position["end"],
                "body": d["value"],
                "entities": [],
            })
    utterance.update({"entities": entities})

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
    return [utterance]
