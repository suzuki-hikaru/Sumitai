from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import SumitaiModel


# Create your views here.

class RegionList(ListView):
    template_name = 'RegionList.html'
    model = SumitaiModel
    
class RegionDetail(DetailView):
    template_name = 'RegionDetail.html'
    model = SumitaiModel