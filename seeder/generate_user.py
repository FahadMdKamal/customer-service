import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mevrik.settings')

import django
django.setup()

## Fake generating script

from django.conf import settings
from django.contrib.auth import get_user_model


from faker import Faker



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
