from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="tasks")
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='task_images/')
    is_deleted=models.BooleanField(default=False)
    
