# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from forms import SignUp, AuthenticationForm, ChildAddForm, ParentAddForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def Start(request):
    print "user is {0}".format(request.user.is_authenticated())
    return render(request, 'login/start.html', {})


def AddUser(request):
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return HttpResponseRedirect('main')
    else:
        form = SignUp()
        return render(request, 'login/signup.html', {'form':form})

def Main(request):
    return render(request, 'login/main.html', {})

def LoginUser(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return render(request, 'login/main.html', {})
        else:
            return render(request, 'login/start.html', {})
    else:
        form = AuthenticationForm()
        return render(request, 'login/login.html', {'form':form})

def ParentAdd(request):
    if request.method == "POST":
        form = ParentAddForm(request.POST)
        parent = form.save()
        parent.save()
        return render(request,'login/parentlist.html', {'id':parent.parent_id})
    else:
        form = ParentAddForm()
        return render(request, 'login/parentadd.html', {'form':form})


def ChildAdd(request):
    if request.method == "POST":
        form = ChildAddForm(request.POST)
        child = form.save()
        child.save()
        return render(request,'login/child.html', {'child':child})
    else:
        form = ChildAddForm()
        return render(request, 'login/childadd.html', {'form':form})


def ChildView(request, pk):
    child = Child.objects.get(pk=pk)
    return render(request,'login/child.html',{'child':child})


def ParentView(request, pk):
    parent = Parent.objects.get(pk=pk)
    return render(request,'login/parent.html',{'parent':parent})


def LogoutUser(request):
    logout(request)
    return render(request, 'login/start.html', {})

