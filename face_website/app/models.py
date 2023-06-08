from django.db import models
from datetime import timedelta
from django.forms import ModelForm


class Event(models.Model):
    upload = models.FileField(upload_to='screenshots/')
    date = models.DateTimeField()
    arotik = models.CharField(max_length=33)
    face = models.CharField(max_length=33)
    ontime = models.BooleanField(null=True)
    minlate = models.DurationField(null=True)

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['date', 'face', 'arotik','ontime', 'minlate','upload']

