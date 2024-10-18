from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    email = models.EmailField(blank=True) 
    due_date = models.DateTimeField(blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
