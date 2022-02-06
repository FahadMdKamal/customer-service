from asyncio.windows_events import NULL
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mevrik.settings')

import django
from faker import Faker
django.setup()

## Fake generating script

from django.conf import settings
from django.contrib.auth import get_user_model

# from users.models import Profile
# from blog.models import Blog, Comment
# from vehicle.models import Vehicle

from django.shortcuts import get_object_or_404
from apps.core.models import Taxonomy

# python manage.py migrate
# python seeder_data.py

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

# app_id = models.CharField(max_length=255)
# taxonomy_type = models.CharField(max_length=50)
# context = models.CharField(max_length=255, null=True, blank=True)
# name = models.CharField(max_length=50, null=True, blank=True)
# description = models.TextField(null=True, blank=True)
# slug = models.SlugField()
# crumbs = models.CharField(max_length=255, null=True, blank=True)
# ref_path = models.CharField(max_length=255, null=True, blank=True)
# parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
# display_order = models.IntegerField(default=0)
# photo_url = models.URLField(null=True, blank=True)
# details = models.CharField(max_length=255, null=True, blank=True)
# status = models.CharField(max_length=10, null=True, blank=True)
def add_wrapper_to_taxonomy(*args, **kwargs):
    return Taxonomy.objects.get_or_create(
        **kwargs

    # app_id = obj_dict['app_id'],
    # taxonomy_type = obj_dict['Complain'],
    # context =  obj_dict['context'],
    # name = obj_dict['Complain'],
    # description = obj_dict['description'],
    # crumbs = None,
    # ref_path = None,
    # parent = None,
    # display_order = None, 
    # photo_url = None,
    # details = None,
    # status = None
    )


# def add_blog():
#     fake_user           = add_user()
#     fake_title          = fakegen.sentences(nb=1, ext_word_list=None)
#     fake_content        = fakegen.text(max_nb_chars=600, ext_word_list=None)
#     fake_topic          = fakegen.pyint(min_value=0, max_value=2, step=1)
#     fake_posted_date    = fakegen.past_date(start_date="-30d", tzinfo=None)
#     blog                = Blog.objects.get_or_create( author= fake_user,
#                                                     title= fake_title, 
#                                                     content= fake_content, 
#                                                     topic = fake_topic,
#                                                     is_approved = True,
#                                                     posted_date = fake_posted_date)[0]
#     print('\n###   blog Created   ###')
#     return blog


# def add_vehicles():
#     fake_owner          = add_user()
#     fake_model_name     = fakegen.pyint(min_value=0, max_value=20, step=1)
#     fake_model_year     = fakegen.past_date(start_date="-1200d", tzinfo=None)
#     fake_reg_no         = fakegen.license_plate()
#     fake_vehicle_type   = fakegen.pyint(min_value=0, max_value=3, step=1)
#     fake_added_on       = fakegen.past_date(start_date="-15d", tzinfo=None)
#     fake_rent           = fakegen.pyint(min_value=2000, max_value=30000, step=1000)
#     fake_capacity       = fakegen.pyint(min_value=2, max_value=35, step=1)
#     fake_is_freezed     = fakegen.pyint(min_value=0, max_value=1, step=1)
#     fake_is_approved    = fakegen.pyint(min_value=0, max_value=1, step=1)
    
#     car                 = Vehicle.objects.get_or_create(owner = fake_owner,
#                                                         model_name = fake_model_name,
#                                                         model_year = fake_model_year,
#                                                         reg_no = fake_reg_no,
#                                                         vehicle_type = fake_vehicle_type,
#                                                         added_on = fake_added_on,
#                                                         rent = fake_rent,
#                                                         capacity = fake_capacity,
#                                                         is_freezed = fake_is_freezed,
#                                                         is_approved = fake_is_approved)

#     owner_profile       = get_object_or_404(Profile, user = fake_owner)
#     owner_profile.user_type = 1
#     owner_profile.save()
    
#     print('\n###   vehicle Created   ###')
#     return car


# def create_comment(N=2):
#     for post in range(N):
#         post                    = add_blog()
#         for entry in range(N):
#             user                = add_user()
#             fake_comment        = fakegen.text(max_nb_chars=256, ext_word_list=None)
#             fake_comment_date   = fakegen.past_date(start_date="-30d", tzinfo=None)
#             Comment.objects.get_or_create(  user=user, 
#                                             blog=post, 
#                                             comment=fake_comment, 
#                                             comment_date = fake_comment_date)
#     print('\n###   comment Created   ###')


def populate_data(N=5):

    for entry in range(N):

        ## Raw Data
        user = add_user() 
        # add_blog()
        # add_vehicles()

        ## Complex Data
        # create_comment()




if __name__ == '__main__':

    # user = User.objects.get_or_create(username= 'admin', 
    #                                 password= make_password("admin123"), 
    #                                 email = 'admin@gmail.com',
    #                                 first_name = 'Super',
    #                                 last_name = 'User',
    #                                 is_staff = True,
    #                                 is_superuser = True,
    #                                 is_active = True )



    print("Super User Created")
    print("#############################################################")  
    # user = User.objects.get_or_create(username= 'Moderator', 
    #                                 password= make_password("password123"), 
    #                                 email = 'moderator@gmail.com',
    #                                 first_name = 'Staff',
    #                                 last_name = 'User',
    #                                 is_staff = True,
    #                                 is_superuser = False,
    #                                 is_active = True )

    print("Moderator Created")
    print("#############################################################")


    print("Populating Data... Please Wait.")
    print("#############################################################")
    # populate_data(20)
    # app_id = models.CharField(max_length=255)
    # taxonomy_type = models.CharField(max_length=50)

    # context = models.CharField(max_length=255, null=True, blank=True)
    # name = models.CharField(max_length=50, null=True, blank=True)
    # description = models.TextField(null=True, blank=True)
    # slug = models.SlugField()
    # crumbs = models.CharField(max_length=255, null=True, blank=True)
    # ref_path = models.CharField(max_length=255, null=True, blank=True)
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    # display_order = models.IntegerField(default=0)
    # photo_url = models.URLField(null=True, blank=True)
    # details = models.CharField(max_length=255, null=True, blank=True)
    # status = models.CharField(max_length=10, null=True, blank=True)
    
    add_wrapper_to_taxonomy()
    print("Populating Data... Complete")
    print("#############################################################")