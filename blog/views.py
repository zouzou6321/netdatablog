from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Artic
# Create your views here.


class ArticListView(ListView):
    model = Artic
    template_name = 'artic.html'

class ArticDetailView(DetailView):
    model = Artic
    template_name = 'artic_detail.html'