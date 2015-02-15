# -*- coding: utf-8 -*-

"""
Copyright 2014-2015 Ratina

@author: Savor d'Isavano
@date: 2015-02-06

Others views.
"""

__author__ = "Savor d'Isavano"

from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'others/index.djhtml'


class SeigiNoMeView(TemplateView):
    template_name = 'others/seigi_no_me.djhtml'


class SeimeiToIshikiNoJyoudanView(TemplateView):
    template_name = 'others/seimei_to_ishiki_no_jyoudan.djhtml'
