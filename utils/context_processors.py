# -*- coding: utf-8 -*-

"""
Copyright 2014-2015 Ratina

@author: Savor d'Isavano
@date: 2015-02-05

Custom context processors.
"""

__author__ = "Savor d'Isavano"

from django.core.urlresolvers import resolve

def app_name(request):
    return {"app_name": resolve(request.path).app_name}
