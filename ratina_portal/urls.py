from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('home.urls', app_name='home')),
    url(r'^blog/', include('blog.urls', app_name='blog')),

    url(r'^admin/', include(admin.site.urls)),
)
