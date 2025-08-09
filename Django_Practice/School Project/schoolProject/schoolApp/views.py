from django.shortcuts import render, redirect
from schoolApp.models import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            CustomUserModel.objects.create_user(
                username = username,
                email = email,
                password = password,
                user_types = 'Admin',
            )
            return redirect('loginPage')
    return render(request, 'signup.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def dashboard(request):
    return render(request, 'dashboard.html')

def profile(request):
    return render(request, 'profile.html')

def addTeacher(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        user = CustomUserModel.objects.create_user(
            username = email,
            password = phone,
            user_types = 'Teacher',
        )
        if user:
            TeacherModel.objects.create(
                user = request.user,
                name = name,
                designation = designation,
                address = address,
                phone = phone,
            )
            return redirect('teacherList')

    return render(request, 'addTeacher.html')

def teacherList(request):
    teacher_info = TeacherModel.objects.all()
    return render(request, 'teacherList.html',{'teachers':teacher_info})