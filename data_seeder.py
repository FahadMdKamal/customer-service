import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mevrik.settings')

from typing import Tuple
import django
django.setup()

from faker import Faker
from django.contrib.auth import get_user_model
from apps.core.models import Taxonomy, Channels, Apps




# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# import django
# django.setup()

# ## Fake generating script

# import random
# from django.conf import settings
# from django.contrib.auth.models import User

# # from users.models import Profile
# # from blog.models import Blog, Comment
# # from vehicle.models import Vehicle

# from faker import Faker
# from django.contrib.auth.hashers import make_password
# from apps.core.models import MavrikApps, MaverikChannels


# fakegen = Faker()













fakegen = Faker()

def add_user():
    return get_user_model().objects.get_or_create(
        username=fakegen.name(),
        password="zxc1ZXC!",
        email=fakegen.email(),
        first_name=fakegen.first_name(),
        last_name=fakegen.last_name(),
        is_staff=False
    )


def _get_random_int(min_value=0, max_value=9, step=1):
    return fakegen.pyint(min_value=min_value, max_value=max_value, step=step)

def _get_model_enum(enums:Tuple):
    enum_num = _get_random_int(max_value=len(enums)-1)
    return enums[enum_num][0]
   
def add_app(kwargs):
    print(kwargs)
    ap = Apps(**kwargs)
    ap.save()
    print(ap.app_name)
    # return Apps.objects.create(**kwargs)
   
def add_channel(*args, **kwargs):
    return Channels.objects.create(**kwargs)

def add_wrapper_to_taxonomy(parent=None, *args, **kwargs):
    if parent:
        kwargs.update({"parent":parent})
    return Taxonomy.objects.create(**kwargs)


    # app_name = models.CharField(max_length=255, unique=True)
    # app_code = models.CharField(max_length=20, unique=True)
    # app_domain = models.CharField(max_length=255, null=True, blank=True)
    # app_config = models.JSONField(default=dict, null=True, blank=True)
    # app_icon = models.CharField(max_length=20, null=True, blank=True)
    # allowed_domains = models.JSONField(default=dict, null=True, blank=True)
    # allowed_channel_types = models.CharField(
    #     choices=CHANNEL_TYPE, 
    #     max_length=10, 
    #     default='facebook'
    # )
    # status = models.CharField(choices=STATUS, max_length=10, default='inactive')
    # slug = models.SlugField(unique=True, null=True, blank=True)

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

def get_abv_code():
    name = fakegen.company()
    code = ""
    for w in name.split(" "):
        code += w[:1].upper()
    code = "-".join(code)+ "-" + str(_get_random_int(1111,9999))
    return name,code



if __name__ == '__main__':
    print("Populating Seeder Data....")

    print("Creating App....")
    print(get_abv_code()[0])
    print(get_abv_code()[1])
    # channel = add_app(kwargs={
    #     "app_name": fakegen.company(),
    #     "app_code": str(_get_random_int(1111,9999)),
    #     "app_domain":"https://www." + fakegen.hostname(),
    #     "allowed_channel_types":_get_model_enum(Apps().CHANNEL_TYPE),
    #     "status":_get_model_enum(Apps().STATUS)
    #     })

    # print("Creating Channel....")
    # channel = add_channel({
    #     "app_id": 1,
    #     "channel_name": fakegen.company(),
    #     "channel_type": _get_model_enum(Channels().CH_TYPES),
    #     "status":_get_model_enum(Channels().STATUS),
    #     "connectivity_status":_get_model_enum(Channels().CONNECTIVITY_STATUS)
    #     })



    print("######################## Message Wrapper Stored #####################################")
    print("Populating Message Wrapper....")
    # obj = add_wrapper_to_taxonomy({"app_id":1,"taxonomy_type":"WRAPPER","name":"Complaint"})
    # add_wrapper_to_taxonomy(parent=obj,kwargs={"app_id":channel,"taxonomy_type":"WRAPPER","name":"Account"})
    # add_wrapper_to_taxonomy(parent=obj,kwargs={"app_id":channel,"taxonomy_type":"WRAPPER","name":"Activate"})
    # add_wrapper_to_taxonomy(parent=obj,kwargs={"app_id":channel,"taxonomy_type":"WRAPPER","name":"De Activate"})
    # add_wrapper_to_taxonomy(parent=obj,kwargs={"app_id":channel,"taxonomy_type":"WRAPPER","name":"Pause"})

    # obj = add_wrapper_to_taxonomy({"app_id":channel,"taxonomy_type":"WRAPPER","name":"Request"})
    # add_wrapper_to_taxonomy(parent=obj,kwargs={"app_id":channel,"taxonomy_type":"WRAPPER","name":"Balance"})
    # add_wrapper_to_taxonomy(parent=obj,kwargs={"app_id":channel,"taxonomy_type":"WRAPPER","name":"Not Showing"})
    # add_wrapper_to_taxonomy(parent=obj,kwargs={"app_id":channel,"taxonomy_type":"WRAPPER","name":"Balance Deduct"})
    # add_wrapper_to_taxonomy(parent=obj,kwargs={"app_id":channel,"taxonomy_type":"WRAPPER","name":"Balance Transfer"})

    # obj = add_wrapper_to_taxonomy({"app_id":channel,"taxonomy_type":"WRAPPER","name":"Query"})
    # add_wrapper_to_taxonomy(parent=obj,kwargs={"app_id":channel,"taxonomy_type":"WRAPPER","name":"Recharge"})
    # add_wrapper_to_taxonomy(parent=obj,kwargs={"app_id":channel,"taxonomy_type":"WRAPPER","name":"How to recharge"})
    # add_wrapper_to_taxonomy(parent=obj,kwargs={"app_id":channel,"taxonomy_type":"WRAPPER","name":"Where to recharge"})
    # add_wrapper_to_taxonomy(parent=obj,kwargs={"app_id":channel,"taxonomy_type":"WRAPPER","name":"Recharge offer"})

    print("######################## Message Wrapper Stored #####################################")
    # populate_data(20)
    print("Populating Data... Complete")
    print("#############################################################")