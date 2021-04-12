from django.conf import settings
from django.shortcuts import (render, redirect)
from django.contrib import messages



def home_redirect_view(request):
    return redirect('overview')


def overview_view(request):    
    return render(request, 'overview.html')


