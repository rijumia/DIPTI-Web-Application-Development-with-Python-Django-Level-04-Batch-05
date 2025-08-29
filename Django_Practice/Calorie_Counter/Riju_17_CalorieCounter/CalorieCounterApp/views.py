from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .models import *
from django.contrib import messages

# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if not username or not email or not password or not confirmPassword:
            messages.error(request, "All fields are required.")
            return redirect('registerPage')

        if CustomUserAuthModel.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('registerPage')

        if CustomUserAuthModel.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('registerPage')

        if password != confirmPassword:
            messages.error(request, "Passwords do not match.")
            return redirect('registerPage')

        user = CustomUserAuthModel.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        if user:
            UserProfileModel.objects.create(user=user)
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('loginPage')

    return render(request, 'register.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Both username and password are required.")
            return redirect('loginPage')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('loginPage')

    return render(request, 'login.html')


def logoutPage(request):
    logout(request)
    return redirect('loginPage')


def dashboard(request):
    return render(request, 'dashboard.html')