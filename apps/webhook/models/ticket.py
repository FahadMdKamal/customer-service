from django.db import models

class Ticket(models.Model):
    message_type = models.CharField(
        max_length=15,
        choices=(
            ('messaging', 'messaging'),
            ('status' , 'status'),
            ('post' , 'post'),
            ('comment' , 'comment'),
            ('reaction' , 'reaction'),
        ),
        default='',
    )
    platform = models.CharField(
        max_length=15,
        choices=(
            ('facebook' , 'facebook'),
            ('instagram' , 'instagram'),
            ('whatsapp' , 'whatsapp'),
            ('web', 'web'),
        ),
        default='',
    )
    source = models.CharField(max_length=200)
    content_id = models.CharField(max_length=200, default='')
    body = models.TextField(default='')
    body_parsed = models.TextField(default='')
    from_type = models.CharField(
        max_length=15,
        choices=(
            ('psid' , 'psid'),
            ('mevrik_id' , 'mevrik_id'),
        ),
        default='',
    )
    from_ref = models.CharField(max_length=200)
    from_name = models.CharField(max_length=200)
    from_photo = models.TextField()
    received_at = models.CharField(max_length=50)
    case_id = models.CharField(max_length=50)
    case_message_id = models.CharField(max_length=50)
    message_direction = models.CharField(max_length=50)
    recipient_ref = models.CharField(max_length=50)
    sent_at = models.CharField(max_length=50)
    reply_to_ref = models.CharField(max_length=50)
    status = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)