from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import news
# Create your views here.


class ArticListView(ListView):
    model = news
    template_name = 'artic.html'

class ArticDetailView(DetailView):
    model = news
    template_name = 'artic_detail.html'