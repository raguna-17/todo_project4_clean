from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0) 

    def __str__(self):
        return self.title
#todo/models.py