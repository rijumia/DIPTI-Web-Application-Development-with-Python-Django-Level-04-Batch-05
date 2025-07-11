from django.shortcuts import render, redirect
from UserAuthApp.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('registerPage')

        if CustomUserModel.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('registerPage')

        if CustomUserModel.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('registerPage')

        user = CustomUserModel.objects.create_user(
            username=username, 
            email=email, 
            password=password1,
            )
        user.save()
        messages.success(request, "Account created successfully.")
        return redirect('loginPage')  

    return render(request, 'register.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('homePage')  # or wherever you want
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('loginPage')

    return render(request, 'login.html')

