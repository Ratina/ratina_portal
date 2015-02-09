# -*- coding: utf-8 -*-

"""
Copyright 2014-2015 Ratina

@author: Savor d'Isavano
@date: 2015-02-09

Blog admin.
"""

__author__ = "Savor d'Isavano"

from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from .models import Author, Post

# Register your models here.

admin.site.register(Author)
admin.site.register(Post, MarkdownModelAdmin)
