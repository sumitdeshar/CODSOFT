from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Todo (models.Model):
    PRIORITY_CHOICES =(
        ('1', 'High Priority'),
        ('2', 'Medium Priority'),
        ('3', 'Low Priority'),
    )
    
    Status = (
        ('1', 'Completed'),
        ('2', 'Pending'),
        ('3', 'Begin'),
    )
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    tuser = models.ForeignKey(User, on_delete=models.CASCADE)
    
    priority = models.CharField( max_length = 20, choices = PRIORITY_CHOICES, default = '3') 
    status = models.CharField( max_length = 20, choices = Status, default = '3')

    def __str__(self):
        return self.title

    