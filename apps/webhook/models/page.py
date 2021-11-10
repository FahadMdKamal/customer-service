from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=60)
    source = models.CharField(
        max_length=15,
        choices=(
            ('facebook' , 'facebook'),
            ('instagram' , 'instagram')
        ),
        default='',
    )
    page_id = models.CharField(max_length=60)
    page_access_token = models.TextField()
    info = models.TextField()
    
    def __str__(self):
        return self.name