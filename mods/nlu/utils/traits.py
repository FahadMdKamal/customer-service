from config.settings import WIT_KEY
from mods.nlu.utils.nlp import Nlp

client = Nlp(access_token=WIT_KEY)


def traits_get_or_create(name, val):
    '''
    Returns the Traits object new create or update Traits in WIT.

            Parameters:
                    name (string): A string string representing the name of Traits
                    val (list): A List of strings representing the name of the Values

            Returns:
                    Response Traits object(JSON object): New create or update Traits
    '''
    try:
        data = client.trait_info(trait_name=name)
    except:
        data = ""

    if data:
        # update with trait_name
        try:
            if isinstance(val, list):
                for i in val:
                    try:
                        resp = client.create_trait_value(trait_name=name, new_value=i)
                    except:
                        pass
            else:
                resp = client.create_trait_value(trait_name=name, new_value=val)
        except:
            resp = {"done"}
    else:
        try:
            if isinstance(val, list):
                resp = client.create_trait(trait_name=name, values=val)
            else:
                resp = client.create_trait(trait_name=name, values=[val])
        except:
            resp = {"done"}

    return resp
