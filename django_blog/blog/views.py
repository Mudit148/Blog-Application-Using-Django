from django.shortcuts import render, redirect
from django.http import HttpResponse
from .import models
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        userr = authenticate(request, username=name, password=password)
        if userr is not None:
            auth_login(request, userr)
            return redirect('/home')
        else:
            return redirect('/login')
    return render(request, 'blog/login.html')


def home(request):
    context = {'posts': Posts.objects.all()}
    return render(request, 'blog/home.html', context)


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('upassword')
        newuser = User.objects.create_user(
            username=name, email=email, password=password)
        newuser.save()
        return redirect("/login")
    return render(request, 'blog/signup.html')

@login_required
def newPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        npost = models.Posts(title=title, content=content, author=request.user)
        npost.save()
        return redirect('/home')
    
    return render(request, 'blog/newPost.html')

@login_required
def myPost(request):
    context = {
        'poss': Posts.objects.filter(author= request.user)
    }
    return render(request, 'blog/myPost.html', context)


def signout(request):
    logout(request)
    return redirect('/login')
