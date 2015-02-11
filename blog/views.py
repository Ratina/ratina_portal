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
from utils.paginator import make_page
from .models import Post


class IndexView(ListView):
    template_name = 'blog/list.djhtml'
    model = Post

    def get_queryset(self):
        post_list = Post.objects.order_by('-created').all()
        page = self.request.GET.get('page')
        posts = make_page(post_list, per_page=5, current_page=page)

        return posts


class PostView(DetailView):
    template_name = 'blog/post.djhtml'
    model = Post


class TagView(ListView):
    template_name = 'blog/list.djhtml'
    model = Post

    def get_queryset(self):
        tag = self.kwargs.get('tag')
        post_list = Post.objects.filter(tags__name=tag)
        page = self.request.GET.get('page')
        posts = make_page(post_list, per_page=5, current_page=page)

        return posts
