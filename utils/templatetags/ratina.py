# -*- coding: utf-8 -*-

"""
Copyright 2014-2015 Ratina

@author: Savor d'Isavano
@date: 2015-02-09

Ratina localized tags and filters.
"""

__author__ = "Savor d'Isavano"

from django import template

register = template.Library()


def rt_date(value):
    return value.strftime('%-Y-%-m-%-d')

def rt_date_cn(value):
    return value.strftime('%-Y年%-m月%-d日')

register.filter('rt_date', rt_date)
register.filter('rt_date_cn', rt_date_cn)
