import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from apps.core.models import PasswordStore
import datetime
from hashlib import sha256


class PasswordPatternValidator:
    """
    Validate whether the password is following the pattern.
    """
    def validate(self, password, user=None):
        regex = re.compile('[@$!%*?#]')
        if not regex.search(password):
            raise ValidationError(
                _("Password do not contains special characters"),
                code='password_pattern_not_matched',
            )

    def get_help_text(self):
        return _('Your password must contain special character(s) @, $, !, %, *, ?, # ')


def is_password_change_valid(user, password):
    user_deatils = user.username + password
    hash_value = sha256( user_deatils.encode("utf-32") ).hexdigest().upper()

    pwd_store = PasswordStore.objects.filter(user=user, hashed_pass=hash_value).first()
    if pwd_store:
        if pwd_store.is_allowed:
            pwd_store.updated_on = datetime.datetime.now()
            pwd_store.save()
        else:
            return False
    else:
        pwd_store = PasswordStore(user=user, hashed_pass=hash_value)
        pwd_store.save()
    return True
