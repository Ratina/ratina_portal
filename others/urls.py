# -*- coding: utf-8 -*-

"""
Copyright 2014-2015 Ratina

@author: Savor d'Isavano
@date: 2015-02-06

Others urls.
"""

__author__ = "Savor d'Isavano"

from django.conf.urls import patterns, include, url
from .views import IndexView


urlpatterns = patterns('',
    url('^$', IndexView.as_view(), name='index'),
)
