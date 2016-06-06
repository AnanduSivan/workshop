from django.conf.urls import patterns, include, url

from django.contrib import admin
from registration.views import Home
from registration import urls as reg_urls
from django.contrib.auth import views as auth_views
from workshop.views import anonymous_required
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^registration/', include(reg_urls)),
                       url(r'^$', Home.as_view(), name='home'),
                       url(r'^user/login/$',
                           anonymous_required(auth_views.login),
                           {'template_name': 'login.html'},
                           name='login'),
                       url(r'^user/logout/$',
                           auth_views.logout,
                           {'template_name': 'logout.html'},
                           name='logout'),
                       )
