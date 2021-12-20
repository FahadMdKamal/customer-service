from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

app_user_model = get_user_model()


class PasswordStoreManager(models.Manager):

    def create(self, user, hash_value):
        pwd_stor = self.model(user=user, password=hash_value )
        pwd_stor.save()

    def is_allowed(self):
        dt = datetime.now()
        return True if (dt - self.model.updated_on).days > 60 else False
        

class PasswordStore(models.Model):
    user = models.OneToOneField(app_user_model, on_delete=models.CASCADE, related_name="passwords")
    password = models.CharField(max_length=255)
    updated_on = models.DateTimeField(auto_now=True)

    objects = PasswordStoreManager()

    class Meta:
        db_table = "user_passwords_store"
    