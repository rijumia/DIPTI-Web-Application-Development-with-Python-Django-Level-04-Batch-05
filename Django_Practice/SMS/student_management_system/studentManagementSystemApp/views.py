from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from studentManagementSystemApp.models import *

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
    return render(request, 'login.html')

def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        hire_date = request.POST.get('hire_date')
        
        userExist = CustomUserModel.objects.filter(username = username).exists()
        if userExist:
            messages.error(request, 'User Already Exists')
            return redirect('signupPage')
        if password == confirm_password:
            user = CustomUserModel.objects.create_user(
                username = username,
                email = email,
                user_type = user_type,
                password = password,
            )
            if user_type == 'Teacher':
                TeacherModel.objects.create(
                    user = user,
                    subject = subject,
                    phone = phone,
                    hire_date = hire_date,
                    )
            return redirect('loginPage')
    return render(request, 'signup.html')

def logOutPage(request):
    logout(request)
    return redirect('loginPage')

def homePage(request):
    return render(request, 'home.html')