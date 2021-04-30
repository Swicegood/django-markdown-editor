from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.shortcuts import (render, redirect)
from django.contrib import messages
from app.models import Event, EventForm
import datetime as dt
from datetime import datetime
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt



def home_redirect_view(request):
    return redirect('overview')

@csrf_exempt
def overview_view(request):
    some_day_last_week = timezone.now().date() - dt.timedelta(days=7)
    monday_of_last_week = some_day_last_week - dt.timedelta(days=(some_day_last_week.isocalendar()[2] - 1))
    monday_of_this_week = monday_of_last_week + dt.timedelta(days=7)    
    date_time_str = None
    if request.method == 'POST':
        event = request.POST.copy() 
        date_time_str = event.get('date',False) 
        date_time_str = date_time_str[:18]
        date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S')
        aroti = get_arotik(date_time_str)
        event['date']=date_time_obj
        event['arotik']=aroti
        event['ontime']=is_arotik_ontime(date_time_obj,aroti)
        event['minlate']=minutes_late(date_time_obj,aroti)
        form = EventForm(event, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/')

    all_events = Event.objects.all()
    past_week_events = all_events.filter(date__gte=some_day_last_week)
    past_week_of_days = break_into_days(past_week_events)
    return render(request, 'overview.html', {'all_events': all_events, 'past_week_of_days':past_week_of_days})
  
 

def break_into_days(past_week_events):
    past_week_of_days = []
    start = past_week_events[0].date
    end = past_week_events[0].date
    for i in range(7):
        end += dt.timedelta(days=1)
        day = past_week_events.filter(date__gte=start, date__lt=end)
        if day:
            past_week_of_days.append(day)
        start = end
    return past_week_of_days


def is_arotik_ontime(date_time_obj, aroti):
    if minutes_late(date_time_obj, aroti) < dt.timedelta(minutes = 5):
        return True
    return False

def minutes_late(date_time_obj, aroti):
    atime = None
    if aroti=="Mangal":
        atime = dt.time(4,30,0)
    if aroti=="Darshan":
        atime = dt.time(7,15,0)
    if aroti=="Noon":
        atime = dt.time(12,30,0)
    if aroti=="Four O'clock":
        atime = dt.time(16,15,0)
    if aroti=="Evening":
        atime = dt.time(19,0,0)
    date1 = date_time_obj.date()
    if not atime:
        return dt.timedelta(seconds=0)
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

def success_view(request):    
    return HttpResponse("Success!")