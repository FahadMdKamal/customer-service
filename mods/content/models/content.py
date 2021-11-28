from django.db import models

FORMAT = (
    ('JSON', 'json'),
    ('BASE64', 'base64'),
    ('TEXT', 'text'),
    ('MARKDOWN', 'markdown'),
)


class ContentManager(models.Manager):
    pass


class Content(models.Model):
    type_ref = models.CharField(max_length=100)
    title = models.CharField(max_length=244)
    subtitle = models.CharField(max_length=244)
    description = models.TextField()
    default_action = models.CharField(max_length=100)
    action_items = models.JSONField()
    parent_id = models.ForeignKey('self', blank=True, null=True, on_delete=models.PROTECT)
    left_contents = models.JSONField()
    display_order = models.CharField(max_length=100)
    content_body = models.JSONField()
    content_format = models.CharField(max_length=100, choices=FORMAT)
    template_cache = models.CharField(max_length=100)
    value_cache = models.CharField(max_length=244)
    last_used_at = models.DateTimeField(auto_now=True)
    objects = ContentManager()

    class Meta:
        db_table = 'converse_content'
