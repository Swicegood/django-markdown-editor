from django.conf import settings
from django.shortcuts import (render, redirect)
from django.contrib import messages
from app.models import Event
from datetime import datetime


def home_redirect_view(request):
    return redirect('overview')


def overview_view(request):    
    context = request.GET.copy() 
    date_time_str = context.get('date',False)
    if not date_time_str:
        date_time_str = "08_01_71_01:00:00"
    date_time_obj = datetime.strptime(date_time_str, '%d_%m_%y_%H:%M:%S')
    d = Event(date=date_time_obj, arotik="mangal", face=context.get('face', False))
    d.save()
    all_events = Event.objects.all()
    return render(request, 'overview.html', {'all_events': all_events})

