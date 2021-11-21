from ..models import StaticDictionary


def group_name_unique(name):
    has_group = StaticDictionary.objects.filter(term_type__icontains="GROUP", term_value=name).exists()
    if has_group:
        return True
    return False


def action_value_unique(name):
    has_group = StaticDictionary.objects.filter(term_type__icontains="ACTION", term_value=name).exists()
    if has_group:
        return True
    return False


def topic_value_unique(name):
    has_group = StaticDictionary.objects.filter(term_type__icontains="TOPIC", term_value=name).exists()
    if has_group:
        return True
    return False


def intent_terms_validated(term_type, term_value):
    has_terms = StaticDictionary.objects.filter(term_type=term_type, term_value=term_value).exists()
    return has_terms
