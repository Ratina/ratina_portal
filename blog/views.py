# -*- coding: utf-8 -*-

"""
Copyright 2014-2015 Ratina

@author: Savor d'Isavano
@date: 2015-02-07

Blog views.
"""

__author__ = "Savor d'Isavano"

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.core.paginator import (
    Paginator, EmptyPage, PageNotAnInteger
)
from django.db.models import Q
from utils.paginator import make_page
from .models import Post


class IndexView(TemplateView):
    template_name = 'blog/index.djhtml'


class PostListView(ListView):
    template_name = 'blog/list.djhtml'
    model = Post

    def get_queryset(self):
        query = self.request.GET.get('q')
        page = self.request.GET.get('page')
        post_list = Post.objects.order_by('-created')
        if query:
            qs = query.split(' ')
            for q in qs:
                post_list = post_list.filter(
                    Q(title__contains=q) |
                    Q(subtitle__contains=q) |
                    Q(content__contains=q)
                )

        posts = make_page(post_list, per_page=5, current_page=page)

        return posts


class PostView(DetailView):
    template_name = 'blog/post.djhtml'
    model = Post


class TagView(ListView):
    template_name = 'blog/list.djhtml'
    model = Post

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        post_list = Post.objects.filter(tags__slug=slug)
        page = self.request.GET.get('page')
        posts = make_page(post_list, per_page=5, current_page=page)

        return posts
