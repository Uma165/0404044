from django.shortcuts import render
from django.views.generic import ListView

from site_cofe.models import Site


class SiteListView(ListView):
    model = Site
    context_object_name = 'sity'
    template_name = 'main.html'