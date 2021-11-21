from django.db import models

F_TYPE = (
    ('SETTING', 'setting'),
    ('FORM', 'form')
)

EDITOR_ENUM = (
    ('TEXT', 'text'),
    ('TEXTAREA', 'textarea'),
    ('DATE', 'date'),
    ('DATERANGE', 'daterange'),
    ('TIME', 'time'),
    ('TIMERANGE', 'timerange'),
)


class ContentCustomFieldsManager(models.Manager):
    pass


class ContentCustomFields(models.Model):
    type_ref = models.CharField(max_length=100)
    field_type = models.CharField(max_length=244, choices=F_TYPE, default='json')
    label = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    field_key = models.CharField(max_length=100)
    field_value = models.CharField(max_length=244, blank=True, null=True)
    validations = models.JSONField(blank=True, null=True)
    choice = models.JSONField(blank=True, null=True)
    editor = models.CharField(max_length=244, choices=EDITOR_ENUM, default="text")
    editor_config = models.JSONField(blank=True, null=True)
    write_once = models.BooleanField()
    handler = models.CharField(max_length=244, blank=True, null=True)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ContentCustomFieldsManager()

    class Meta:
        db_table = 'converse_content_custom_fields'
