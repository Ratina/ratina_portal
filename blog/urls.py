# -*- coding: utf-8 -*-

"""
Copyright 2014-2015 Ratina

@author: Savor d'Isavano
@date: 2015-02-07

Blog urls.
"""

__author__ = "Savor d'Isavano"

from django.conf.urls import patterns, include, url
from .views import PostListView, PostView, TagView

urlpatterns = patterns(
    '',
#    url('^(p(?P<page>))?$', IndexView.as_view(), name='index')
    url('^$', PostListView.as_view(), name='index'),
    url('^fictional-world/$', PostListView.as_view(), name='fw'),
    url('^conlang/$', PostListView.as_view(), name='cl'),
    url('^programming/$', PostListView.as_view(), name='programming'),
    url('^tag/(?P<slug>.+)/$', TagView.as_view(), name='tag'),
    url('^p/(?P<slug>.+)/$', PostView.as_view(), name='detail'),
)
