#from django.shortcuts import render

from django.views.generic import DetailView, ListView

from .models import Grap

class GrapDetailView(DetailView):
    model = Grap
    
class GrapListView(ListView):
    model = Grap

