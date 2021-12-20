import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class PasswordPatternValidator:
    """
    Validate whether the password is following the pattern.
    """
    def validate(self, password, user=None):
        if not re.match(r"""^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?#])[A-Za-z\d@$!%*?#]{8,}$""", password):
            raise ValidationError(
                _("Password must contain one of [A-Z] & [a-z] & [0-9] & [@$!%*?#]"),
                code='password_pattern_not_matched',
            )

    def get_help_text(self):
        return _('Password must contain one capital, one lower, one digit and a special character (@ $ ! % * ? #)')
