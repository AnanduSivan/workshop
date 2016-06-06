
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from registration import views
from registration.views import *
from registration.models import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
urlpatterns = [
url(r'^$', UserRegistrationView.as_view(), name='user_signup'),
    url(r'^user/success/', TemplateView.as_view(template_name='success.html'),
        name='page')
]
