from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
from .models import *

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return render(request, 'dashboard.html')
        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')