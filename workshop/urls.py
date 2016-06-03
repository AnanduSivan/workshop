from django.conf.urls import patterns, include, url

from django.contrib import admin
from registration.views import Home
from registration import urls as reg_urls
from workshop.views import anonymous_required
from django.contrib.auth import views as auth_views
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', include(reg_urls)),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^user/login/$',
        anonymous_required(auth_views.login),
        {'template_name': 'login.html'},
         name='login')
)

