# -*- coding: utf-8 -*-

"""
Copyright 2014-2015 Ratina

@author: Savor d'Isavano
@date: 2015-02-07

Blog views.
"""

__author__ = "Savor d'Isavano"

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import (
    Paginator, EmptyPage, PageNotAnInteger
)
from .models import Post


class IndexView(ListView):
    template_name = 'blog/list.djhtml'
    model = Post

    def get_queryset(self):
        post_list = Post.objects.all()
        paginator = Paginator(post_list, 5)

        page = self.request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return posts


class PostView(DetailView):
    template_name = 'blog/post.djhtml'
    model = Post
