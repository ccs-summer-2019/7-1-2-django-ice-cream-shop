from django.shortcuts import render
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = 'brochure/index.html'

class AboutView(generic.TemplateView):
    template_name = 'brochure/about.html'
