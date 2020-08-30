from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import SumitaiModel,ChatModel
from django.urls import reverse_lazy


# Create your views here.
class Top(ListView):
    template_name = 'Top.html'
    model = SumitaiModel

class RegionForm(ListView):
    template_name = 'RegionForm.html'
    model = SumitaiModel

class RegionList(ListView):
    template_name = 'RegionList.html'
    model = SumitaiModel
    
class RegionDetail(DetailView):
    template_name = 'RegionDetail.html'
    model = SumitaiModel

class HouseList(ListView):
    template_name = 'HouseList.html'
    model = SumitaiModel

class HouseDetail(ListView):
    template_name = 'HouseDetail.html'
    model = SumitaiModel

class Request(ListView):
    template_name = 'Request.html'
    model = SumitaiModel

class ChatCreate(CreateView,ListView):
    template_name = 'ChatCreate.html'
    model = ChatModel
    fields = ('userName','chat')
    success_url = reverse_lazy('chatcreate')

class Login(ListView):
    template_name = 'Login.html'
    model = SumitaiModel

class ContractPhone(ListView):
    template_name = 'ContractPhone.html'
    model = SumitaiModel

class ContractView(ListView):
    template_name = 'ContractView.html'
    model = SumitaiModel