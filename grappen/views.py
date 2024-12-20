#from django.shortcuts import render

from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Grap

class GrapCreateView(CreateView):
    model = Grap
    fields = ['vraag', 'antwoord']

class GrapDetailView(DetailView):
    model = Grap

class GrapListView(ListView):
    model = Grap

class GrapUpdateView(UpdateView):
    model = Grap
    fields = ['vraag', 'antwoord']

