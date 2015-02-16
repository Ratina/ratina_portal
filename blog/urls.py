# -*- coding: utf-8 -*-

"""
Copyright 2014-2015 Ratina

@author: Savor d'Isavano
@date: 2015-02-07

Blog urls.
"""

__author__ = "Savor d'Isavano"

from django.conf.urls import patterns, include, url
from .views import (
    PostListView,
    PostView,
    TagListView,
    TagView,
    FictionalWorldView,
    ConlangView,
    OSView,
    ProgrammingView
)

urlpatterns = patterns(
    '',
#    url('^(p(?P<page>))?$', IndexView.as_view(), name='index')
    url('^$', PostListView.as_view(), name='index'),
    url('^fictional-world/$', FictionalWorldView.as_view(), name='fw'),
    url('^conlang/$', ConlangView.as_view(), name='cl'),
    url('^os/$', OSView.as_view(), name='os'),
    url('^programming/$', ProgrammingView.as_view(), name='programming'),
    url('^tag/$', TagListView.as_view(), name='taglist'),
    url('^tag/(?P<slug>.+)/$', TagView.as_view(), name='tag'),
    url('^p/(?P<slug>.+)/$', PostView.as_view(), name='detail'),
)
