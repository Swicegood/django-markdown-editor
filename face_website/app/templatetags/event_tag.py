from django import template
from django.template import Library
from django.template.defaultfilters import stringfilter
from datetime import datetime

register = Library()

@register.simple_tag
def check_if_event_ontime(one_days_events, aroti):
    value =  [event for event in one_days_events if (event.arotik==aroti and event.ontime)]  
    if value:      
        return True
    return False

@register.simple_tag
def get_event(one_days_events):
    if one_days_events:
        return one_days_events[0].date.strftime('%b %d')
    else:
        return None

@register.simple_tag
def get_minlate(one_days_events, arotik):
    one_arotis_events = one_days_events.filter(arotik=arotik)
    if one_arotis_events:
        s = one_arotis_events[0].minlate.seconds
        return int(s/60)
    else:
        return None


@register.filter
@stringfilter
def split(value):
    return value.split(',')