from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import SumitaiModel,ChatModel
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
class Top(ListView):
    template_name = 'Top.html'
    model = SumitaiModel

class RegionForm(ListView):
    template_name = 'RegionForm.html'
    model = SumitaiModel

def RegionList(request):
    object_list = SumitaiModel.objects.all()
    return render(request, 'RegionList.html', {'object_list':object_list})
    
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

def Login(request):
    if request.method == 'POST':
        print("これはPOSTメソッドです")
        postUsername = request.POST['username']
        postMail = request.POST['mail']
        postPassword = request.POST['password']
        user = authenticate(request, username=postUsername, password=postPassword)

        if user is not None:
            login(request, user)
            return redirect('chatcreate')
        # Redirect to a success page.
        else:
            return render(request, 'Login.html', {'error':'このアカウントは登録されていません'})
        # Return an 'invalid login' error message.

    return render(request, 'Login.html')

def Signup(request):
    # user2 = User.objects.all()
    # user2 = User.objects.get(username='hikaru')
    # print(user2)
    # print(user2.email)

    if request.method == 'POST':
        print("これはPOSTメソッドです")
        postUsername = request.POST['username']
        postMail = request.POST['mail']
        postPassword = request.POST['password']
        try:
            User.objects.get(username=postUsername)
            return render(request, 'Signup.html', {'error':'このユーザ名は既に登録されています'}) #本当はメールアドレスの重複をチェックしたい
        except:
            user = User.objects.create_user(postUsername, postMail, postPassword)
            print(request.POST)
            return redirect('login')
    else:
        print("これはGETメソッドです")
    return render(request, 'Signup.html', {'some':100})

def Login(request):
    if request.method == 'POST':
        print("これはPOSTメソッドです")
        postUsername = request.POST['username']
        postMail = request.POST['mail']
        postPassword = request.POST['password']
        user = authenticate(request, username=postUsername, password=postPassword)

        if user is not None:
            login(request, user)
            return redirect('chatcreate')
        # Redirect to a success page.
        else:
            return render(request, 'Login.html', {'error':'このアカウントは登録されていません'})
        # Return an 'invalid login' error message.

    return render(request, 'Login.html')

def Signup(request):
    # user2 = User.objects.all()
    # user2 = User.objects.get(username='hikaru')
    # print(user2)
    # print(user2.email)

    if request.method == 'POST':
        print("これはPOSTメソッドです")
        postUsername = request.POST['username']
        postMail = request.POST['mail']
        postPassword = request.POST['password']
        try:
            User.objects.get(username=postUsername)
            return render(request, 'Signup.html', {'error':'このユーザ名は既に登録されています'}) #本当はメールアドレスの重複をチェックしたい
        except:
            user = User.objects.create_user(postUsername, postMail, postPassword)
            print(request.POST)
            return redirect('login')
    else:
        print("これはGETメソッドです")
    return render(request, 'Signup.html', {'some':100})

# @login_required　関数じゃないとできない
class ChatCreate(CreateView,ListView):
    template_name = 'ChatCreate.html'
    model = ChatModel
    fields = ('userName','chat')
    success_url = reverse_lazy('chatcreate')

# @login_required　関数じゃないとできない
class ContractPhone(ListView):
    template_name = 'ContractPhone.html'
    model = SumitaiModel

# @login_required　関数じゃないとできない
class ContractView(ListView):
    template_name = 'ContractView.html'
    model = SumitaiModel

def Logout(request):
    logout(request)
    return redirect('top')