from django.conf.urls import patterns, include, url
from .views import IndexView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView.as_view(), name='index'),
)
