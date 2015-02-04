from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    app_name = None
    template_name = "home.jinja"
