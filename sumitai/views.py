from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import SumitaiModel,ChatModel
from django.urls import reverse_lazy


# Create your views here.

class RegionList(ListView):
    template_name = 'RegionList.html'
    model = SumitaiModel
    
class RegionDetail(DetailView):
    template_name = 'RegionDetail.html'
    model = SumitaiModel

class ChatCreate(CreateView,ListView):
    template_name = 'ChatCreate.html'
    model = ChatModel
    fields = ('userName','chat')
    success_url = reverse_lazy('chat')