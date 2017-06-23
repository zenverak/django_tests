# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from forms import SignUp, AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def AddUser(request):
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(new_user)
            return HttpResponseRedirect('main.html')
    else:
        form = SignUp()
        return render(request, 'login/signup.html', {'form':form})

def Main(request):
    return render(request, 'login/main.html', {})


def ParentAdd(request):
    if request.method == "POST":
        form = ParentAdd(request.POST)
        parent = form.save()
        parent.save()
        return render(request,'parentlist.html', {'id':parent.parent_id})
    else:
        form = ParentAdd()
        return render(reqeust, 'parentadd.html', {'form':form})


def ChildAdd(request):
    if request.method == "POST":
        form = ChildAdd(request.POST)
        child = form.save()
        child.save()
        return render(request,'child.html', {'child':child})
    else:
        form = ChildAdd()
        return render(reqeust, 'childadd.html', {'form':form})

def ChildView(request, pk):
    child = Child.objects.get(pk=pk)
    return render(request,'child.html',{'child':child})


def ParentView(request, pk):
    parent = Parent.objects.get(pk=pk)
    return render(request,'parent.html',{'parent':parent})    
