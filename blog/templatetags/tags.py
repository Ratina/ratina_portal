# -*- coding: utf-8 -*-

"""
Copyright 2014-2015 Ratina

@author: Savor d'Isavano
@date: 2015-02-09

Tags as a part of the blog layout.
"""

__author__ = "Savor d'Isavano"

from django import template
from django.db.models import Count
from taggit.models import Tag
from ..models import Post

register = template.Library()


@register.assignment_tag
def get_tags(count=None):
    tags = Tag.objects.annotate(
        Count('taggit_taggeditem_items')
    ).extra(select={'lower_name':'lower(name)'}).filter(
        taggit_taggeditem_items__count__gt=0
    ).order_by('-taggit_taggeditem_items__count', 'lower_name')
    if count is not None:
        tags = tags[:count]
    return [
        (t.name, t.slug, t.taggit_taggeditem_items__count)
        for t in tags
    ]
