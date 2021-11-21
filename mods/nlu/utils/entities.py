from config.settings import WIT_KEY
from mods.nlu.utils.formatter import text_uppercase
from mods.nlu.utils.nlp import Nlp

client = Nlp(access_token=WIT_KEY)


def entity_get_or_create(name, roles):
    '''
    Returns the Entity object new create or update entity in WIT.

            Parameters:
                    name (string): A string string representing the name of Entity
                    roles (list): A List of strings representing the name of the roles

            Returns:
                    Response entity (JSON object): New create or update entity
    '''
    data = ""
    name = text_uppercase(name)
    try:
        data = client.entity_info(entity_name=name)
    except:
        data = ""
    if data:
        wit_roles = []
        # update with new roles
        for rl in data["roles"]:
            wit_roles.append(rl["name"].upper())
        for i in roles:
            wit_roles.append(text_uppercase(i))
        try:
            resp = client.update_entity(current_entity_name=name, new_entity_name=name, roles=wit_roles)
        except:
            resp = {"done"}
    else:
        # create new entity and roles
        try:
            resp = client.create_entity(entity_name=name, roles=roles)
        except:
            resp = {"done"}
    return resp
