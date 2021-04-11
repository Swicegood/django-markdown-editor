efrom django.urls import path

from app.views import (home_redirect_view, simple_form_view,
                       post_form_view, test_markdownify)

urlpatterns = [
    path('', home_redirect_view, name='home_redirect'),
    path('overview/', simple_form_view, name='simple_form'),
    
]
