# -*- coding: utf-8 -*-

"""
Copyright 2014-2015 Ratina

@author: Savor d'Isavano
@date: 2015-02-09

Blog admin.
"""

__author__ = "Savor d'Isavano"

from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin, MarkdownInlineAdmin
from .models import Author, Post, PostFile

# Register your models here.

class PostFileInline(admin.StackedInline):
    model = PostFile


class PostAdmin(MarkdownModelAdmin):
    list_display = ['title', 'author']
    inlines = [PostFileInline,]


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
