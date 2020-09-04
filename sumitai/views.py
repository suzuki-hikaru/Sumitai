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

def HouseList(request):
    object_list = SumitaiModel.objects.all()
    return render(request, 'HouseList.html', {'object_list':object_list})

def HouseDetail(request, pk):
    object = SumitaiModel.objects.get(pk=pk)
    return render(request, 'HouseDetail.html', {'object':object})

class Request(ListView):
    template_name = 'Request.html'
    model = SumitaiModel

def Login(request):
    if request.method == 'POST':
        print("これはPOSTメソッドです")
        postUsername = request.POST['username']
        postMail = request.POST['mail']
        postPassword = request.POST['password']
        user = authenticate(request, username=postUsername, mail=postMail, password=postPassword)

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

def RegionForm1(request):
    if request.method =='POST':
        postForm1 = request.POST['form1']
        object_list = SumitaiModel.objects.all
        houseName = object_list.houseName
        try:
            object_form = SumitaiModel.objects.get(houseName=postForm1)
            return render(request, 'RegionList.html', {'object_form':object_form})
        except:
            return render(request, 'RegionForm.html', {'error':'検索結果に一致する地域はありません'})
    else:
        return render(request, 'RegionForm.html')


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

def Good(request, pk):
    object = SumitaiModel.objects.get(pk=pk)
    object.good = object.good +1
    object.save()
    return redirect('houselist')

def Read(request, pk):
    post = SumitaiModel.objects.get(pk=pk)
    loginname = request.user.get_username()
    if loginname in str(post.readtext):
        if post.pushuser == 1:
            post.pushuser = 0
            post.read -= 1
            post.save()
        return redirect('houselist')
    else:
        post.read += 1
        post.pushuser = 1
        post.readtext = str(post.readtext) + ' ' + str(post2)
        post.save()
        return redirect('houselist')