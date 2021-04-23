from django.db import models
from datetime import timedelta


class Event(models.Model):
    date = models.DateTimeField()
    arotik = models.CharField(max_length=33)
    face = models.CharField(max_length=33)
    ontime = models.BooleanField(null=True)
    # minlate = models.DurationField(default=timedelta())
