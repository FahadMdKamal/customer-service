from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Organizations"
    
    def __str__(self) -> str:
        return self.name

