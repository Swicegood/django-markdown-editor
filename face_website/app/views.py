from django.conf import settings
from django.shortcuts import (render, redirect)
from django.contrib import messages



def home_redirect_view(request):
    return redirect('overview')


def overview_view(request):    
    d = request.GET
    print(d)
    return render(request, 'overview.html')


