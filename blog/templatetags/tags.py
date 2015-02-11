# -*- coding: utf-8 -*-

"""
Copyright 2014-2015 Ratina

@author: Savor d'Isavano
@date: 2015-02-09

Tags as a part of the blog layout.
"""

__author__ = "Savor d'Isavano"

from django import template
from taggit.models import Tag
from ..models import Post

register = template.Library()


@register.assignment_tag
def get_tags():
    return [
        (t.name, t.slug, Post.objects.filter(tags__name=t).count())
        for t in Tag.objects.order_by('name')
    ]
