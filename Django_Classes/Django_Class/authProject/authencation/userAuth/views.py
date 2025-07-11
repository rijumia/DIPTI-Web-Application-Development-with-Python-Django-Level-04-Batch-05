from django.shortcuts import render, redirect
from userAuth.models import UserAuthModel
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def registration(request):
    if request.method == 'POST':
        fullname = request.POST.get('FullName')
        username = request.POST.get('UserName')
        email = request.POST.get('Email')
        contact = request.POST.get('ContactNo')
        password = request.POST.get('Password')
        confirm_password = request.POST.get('ConfirmPassword')

        if password == confirm_password:
            userinfo = UserAuthModel.objects.create(
            UserName = fullname,
            FullName = username,
            Email = email,
            ContactNo = contact,
            Password = password
            )
            userinfo.save()
            return redirect('login')
        else:
            print("Password Don't Match")

    return render(request, 'registration.html')

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')