from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from app.views import (home_redirect_view, overview_view)

urlpatterns = [
    path('', home_redirect_view, name='home_redirect'),
    path('overview/', overview_view, name='overview'),    
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
]
