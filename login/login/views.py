# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from forms import SignUp, AuthenticationForm, ChildAddForm, ParentAddForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from numpy.random import randint
from models import RandIds, Parent, Child


def Start(request):
    print "user is {0}".format(request.user.is_authenticated())
    return render(request, 'login/start.html', {})


def AddUser(request):
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return render(request, 'login/main.html', {})
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
                new_id = RandIds(id_number = num)
                new_id.save()
                break
        return num


    if request.method == "POST":
        form = ParentAddForm(request.POST)
        parent = form.save(commit=False)
        parent.parent_id = _get_new_id()
        parent.save()
        return redirect('parentview', parent.parent_id)
    else:
        form = ParentAddForm()
        return render(request, 'login/parentadd.html', {'form':form})


def ChildAdd(request):
    if request.method == "POST":
        form = ChildAddForm(request.POST)

        print "child's parent is {0}".format(request.POST)
        child = form.save(commit=False)
        parent = Parent.objects.get(parent_id=str(request.POST['parent']))
        child.parent_of_child = parent
        child.save()
        return redirect('childview', pk = child.pk)
    else:
        form = ChildAddForm()
        return render(request, 'login/childadd.html', {'form':form})


def ChildView(request, pk):
    child = Child.objects.get(pk=pk)
    return render(request,'login/child.html',{'child':child})


def ParentView(request, parent_id):
    print "parent id is {0} and its type is {1}".format(parent_id, type(parent_id))
    parent = Parent.objects.get(parent_id=str(parent_id))
    children = Child.objects.filter(parent_of_child=parent)
    if len(children) == 0:
        children = ''
    print "child is {0}".format(children)
    info = {'parent':parent, 'children':children}
    return render(request,'login/parent.html',{'info':info})

def ParentList(request):
    parents = Parent.objects.all()
    return render(request, 'login/parentlist.html', {'parents':parents})


def ChildList(request):
    children = Child.objects.all()
    return render(request, 'login/childlist.html', {'children': children})


def LogoutUser(request):
    logout(request)
    return render(request, 'login/start.html', {})

