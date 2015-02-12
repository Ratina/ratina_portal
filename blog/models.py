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
from django.utils.text import slugify
from django.conf import settings
import itertools
import re
import uuid
import os
from .utils import ext_markdown


class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey('Author')
    content = MarkdownField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    tags = TaggableManager(blank=True)

    @property
    def content_ext(self):
        return ext_markdown(self, self.content)

    @property
    def excerpt(self):
        r = re.compile(r'(?P<excerpt>(.|\r?\n){200}(.|\r?\n)*?)(\r?\n){2}', re.U)
        content = ext_markdown(self, self.content)

        m = re.match(r, content)
        if m:
            return "{}...".format(m.group('excerpt'))
        return content

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        if self.slug:
            return reverse('blog:detail', args=[self.slug])
        else:
            return reverse('blog:detail', args[self.pk])

    def __str__(self):
        if self.subtitle:
            return "{} -- {}".format(self.title, self.subtitle)
        else:
            return self.title


def get_file_path(instance, filename):
    name, extension = os.path.splitext(filename)
    return "post/{}{}".format(uuid.uuid4().hex, extension)


class PostFile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to=get_file_path)
    post = models.ForeignKey(Post, related_name='files')

    def save(self):
        if self.pk:
            old = PostFile.objects.filter(pk=self.pk)[:1]
            if old:
                old = old[0]
                if self.file.url != old.file.url:
                    old.file.delete(False)

        return super().save()


class Author(models.Model):
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars', blank=True)

    def __str__(self):
        if self.display_name:
            return "{} <{}>".format(self.name, self.display_name)
        else:
            return self.name


# Signals

from django.db.models.signals import post_delete, post_save
from django.dispatch.dispatcher import receiver

@receiver(post_delete, sender=PostFile)
def postfile_post_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.file.delete(False)
