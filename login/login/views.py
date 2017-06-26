# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from forms import SignUp, AuthenticationForm, ChildAddForm, ParentAddForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from numpy.random import randint
from models import RandIds


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

    def _random_id():
        pre_num = randint(0,10,8)
        str_int = ''
        for num in pre_num:
            str_int = str_int + str(num)
        return str_int

    def _get_new_id():
        num = ''
        while True:
            num = _random_id()
            if RandIds.objects.filter(id_number=num).count() == 0:
                break
        return num
    if request.method == "POST":
        form = ParentAddForm(request.POST)
        parent = form.save(commit=False)
        parent.parent_id = _get_new_id()
        parent.save()
        return render(request, 'login/parent.html', {'parent':parent})
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

