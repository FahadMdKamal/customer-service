from django.db import models


TOPICS=(
    ('social','Social'),
    ('email','Email'),
    ('live_chat','Live_Chat'),
    ('live_call','Live_Call'),
    ('support','Support')
)
DIRECTION = (
    ('fifo','FIFO'),
    ('lifo','LIFO')
)


class QueueTopics(models.Model):
    app_id = models.IntegerField()
    topic = models.SlugField(
        max_length=40,
        choices= TOPICS,
        default='social',
    )
    allowed_source=models.CharField(
        max_length=100,
        default='',
        null= True,
        blank=True
    )
    push_direction =  models.CharField(
        max_length=20,
        choices= DIRECTION,
        default='fifo',
        null= True,
        blank=True
    )
    escalation_timeout = models.IntegerField(default=0,blank=True)
    dispute_timeout = models.IntegerField(default=0,blank=True)
    status = models.CharField(
        max_length=20,
        default='open',
        null= True,
        blank=True
    )
    last_open_at = models.DateTimeField(null= True, blank=True)
    last_closed_at = models.DateTimeField(null= True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        db_table = "mevrik_queue_topics"

