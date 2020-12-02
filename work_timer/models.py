from django.db import models

# Create your models here.

class Timer(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField(auto_now_add=True)
    duration = models.TimeField()