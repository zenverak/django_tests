# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from forms import SignUp, AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect

def AddUser(request):
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            new_user = user.objects.create_user(**form.cleaned_data)
            login(new_user)
            return HttpResponseRedirect('main.html')
    else:
        form = SignUp()
        return render(request, 'singup.html', {'form':form})

def Main(request):
    return render(request, 'main.html', {})
