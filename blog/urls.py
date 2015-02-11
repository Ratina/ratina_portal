# -*- coding: utf-8 -*-

"""
Copyright 2014-2015 Ratina

@author: Savor d'Isavano
@date: 2015-02-07

Blog urls.
"""

__author__ = "Savor d'Isavano"

from django.conf.urls import patterns, include, url
from .views import IndexView, PostView, TagView

urlpatterns = patterns(
    '',
#    url('^(p(?P<page>))?$', IndexView.as_view(), name='index')
    url('^$', IndexView.as_view(), name='index'),
    url('^tag/(?P<tag>.+)/$', TagView.as_view(), name='tag'),
    url('^(?P<slug>.+)/$', PostView.as_view(), name='detail'),
)
