from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        user_type = request.POST.get('userType')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')

        if CustomUserModel.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'register.html')

        if CustomUserModel.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return render(request, 'register.html')

        user = CustomUserModel.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        if user:
            ProfileModel.objects.create(
                user = user,
            )
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('loginPage')  

    return render(request, 'register.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard')  
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')

def changePassword(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        user = request.user

        if not user.check_password(current_password):
            messages.error(request, "Current password is incorrect.")
            return render(request, 'changePassword.html')

        if new_password != confirm_password:
            messages.error(request, "New passwords do not match.")
            return render(request, 'changePassword.html')

        user.set_password(new_password)
        user.save()

        update_session_auth_hash(request, user)

        messages.success(request, "Password changed successfully.")
        return redirect('dashboard') 

    return render(request, 'changePassword.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def profile(request):
    return render(request, 'profile.html')

def updateProfile(request):
    profile = request.user.profile 

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile') 
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'updateProfile.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')