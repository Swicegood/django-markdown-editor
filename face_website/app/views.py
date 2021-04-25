from django.conf import settings
from django.shortcuts import (render, redirect)
from django.contrib import messages
from app.models import Event
import datetime as dt
from datetime import datetime


def home_redirect_view(request):
    return redirect('overview')


def overview_view(request):    
    event = request.GET.copy() 
    date_time_str = event.get('date',False) 
    if not date_time_str:
        date_time_str = "1971-01-08T08:00:00"
        all_events = Event.objects.all()
        return render(request, 'overview.html', {'all_events': all_events})
    date_time_str = date_time_str[:18]
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S')
    aroti = get_arotik(date_time_str)
    d = Event(
        date=date_time_obj,
        arotik=aroti,
        face=event.get('face', False),
        ontime=is_arotik_ontime(date_time_obj,aroti),
        minlate=minutes_late(date_time_obj,aroti)
        )
    d.save()
    all_events = Event.objects.all()
    return render(request, 'overview.html', {'all_events': all_events})

def is_arotik_ontime(date_time_obj, aroti):
    if minutes_late(date_time_obj, aroti) < dt.timedelta(minutes = 5):
        return True
    return False

def minutes_late(date_time_obj, aroti):
    if aroti=="Mangal":
        atime = dt.time(4,30,0)
    if aroti=="Darshan":
        atime = dt.time(7,15,0)
    if aroti=="Noon":
        atime = dt.time(12,30,0)
    if aroti=="Four O'clock":
        atime = dt.time(4,15,0)
    if aroti=="Evening":
        atime = dt.time(7,0,0)
    date1 = date_time_obj.date()
    adatetime = dt.datetime.combine(date1, atime)
    return date_time_obj - adatetime


def get_arotik(date_time_str):
    t = date_time_str.split('T')[-1]
    t = t.split(':')
    start = dt.time(3,25,0)
    end = dt.time(5,0,0)
    x = dt.time(int(t[0]),int(t[1]),int(t[2]))
    if time_in_range(start,end,x):
        return "Mangal"
    start = dt.time(7,0,0)
    end = dt.time(8,0,0)
    if time_in_range(start,end,x):
        return "Darshan"
    start = dt.time(12,0,0)
    end = dt.time(13,0,0)
    if time_in_range(start,end,x):
        return "Noon"
    start = dt.time(16,0,0)
    end = dt.time(17,0,0)
    if time_in_range(start,end,x):
        return "Four O'clock"
    start = dt.time(18,45,0)
    end = dt.time(21,0,0)
    if time_in_range(start,end,x):
        return "Evening"
    else:
        return "Unknown"


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end