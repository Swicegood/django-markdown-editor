from django.db import models


class Event(models.Model):
    date = models.DateTimeField()
    arotik = models.CharField(max_length=33)
    face = models.CharField(max_length=33)

