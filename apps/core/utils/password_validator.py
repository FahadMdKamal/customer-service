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
        if not re.match(r"""^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?#])[A-Za-z\d@$!%*?#]{6,}$""", password):
            raise ValidationError(
                _("Password must contain one of [A-Z] & [a-z] & [0-9] & [@$!%*?#]"),
                code='password_pattern_not_matched',
            )

    def get_help_text(self):
        return _('Password must contain one capital, one lower, one digit and a special character (@ $ ! % * ? #)')


def is_password_change_valid(user, password):
    user_deatils = user.username + password
    hash_value = sha256( user_deatils.encode("utf-32") ).hexdigest().upper()

    pwd_store = PasswordStore.objects.filter(user=user, password=hash_value)
    if pwd_store:
        if pwd_store.objects.is_allowed():
            pwd_store.updated_on = datetime.datetime.now()
            pwd_store.save()
        else:
            return False
    else:
        # TODO: Is Causing the problems
        PasswordStore.objects.create(user=user, hash_value=hash_value)
    return True
