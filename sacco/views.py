from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.
class Dashboard(TemplateView):
    template_name='web/dashboard/home/home.html'
# Create your views here.
