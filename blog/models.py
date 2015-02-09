# -*- coding: utf-8 -*-

"""
Copyright 2014-2015 Ratina

@author: Savor d'Isavano
@date: 2015-02-07

Blog models.
"""

__author__ = "Savor d'Isavano"

from django.db import models
from django_markdown.models import MarkdownField
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey('Author')
    content = MarkdownField()
    date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    @property
    def excerpt(self):
        return self.content

    def __str__(self):
        if self.subtitle:
            return "{} -- {}".format(self.title, self.subtitle)
        else:
            return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars')

    def __str__(self):
        if self.display_name:
            return "{} <{}>".format(self.name, self.display_name)
        else:
            return self.name
