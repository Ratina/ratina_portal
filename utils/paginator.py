# -*- coding: utf-8 -*-

"""
Copyright 2014-2015 Ratina

@author: Savor d'Isavano
@date: 2015-02-09

Paginator helpers
"""

__author__ = "Savor d'Isavano"


from django.core.paginator import (
    Paginator, EmptyPage, PageNotAnInteger
)


def make_page(object_list, *, per_page=5, current_page=1):
    paginator = Paginator(object_list, per_page)

    try:
        objects = paginator.page(current_page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    return objects
