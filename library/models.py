# models.py
from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    participants = models.ManyToManyField('auth.User', related_name='events')

    def __str__(self):
        return self.name
