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
    type_ref = models.CharField(max_length=100, blank=True, null=True)
    app_id = models.CharField(max_length=244, blank=True, null=True)
    title = models.CharField(max_length=244, blank=True, null=True)
    subtitle = models.CharField(max_length=244, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    default_action = models.CharField(max_length=100,blank=True, null=True)
    action_items = models.JSONField(blank=True, null=True)
    parent_id = models.ForeignKey('self', blank=True, null=True, on_delete=models.PROTECT, related_name="content_child_set")
    left_contents = models.JSONField(blank=True, null=True)
    display_order = models.CharField(max_length=100,blank=True, null=True)
    content_body = models.JSONField(blank=True, null=True)
    content_format = models.CharField(max_length=100, choices=FORMAT, blank=True, null=True)
    template_cache = models.CharField(max_length=100,blank=True, null=True)
    value_cache = models.CharField(max_length=244,blank=True, null=True)
    last_used_at = models.DateTimeField(auto_now=True)
    objects = ContentManager()

    class Meta:
        db_table = 'converse_content'
