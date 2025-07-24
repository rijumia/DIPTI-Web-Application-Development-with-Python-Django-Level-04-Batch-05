from django.shortcuts import render,redirect
from userAuthApp.models import userAuthModel
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.hashers import check_password

# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        confirm_password = request.POST.get('Confirm_Password')
        user_types = request.POST.get('user_types')
        
        if password == confirm_password:
            userAuthModel.objects.create_user(
                username=username, 
                email=email, 
                password=password, 
                user_types=user_types
                )
            return redirect('loginPage')
    return render(request, 'register.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.user.user_types == 'recruiter':
                return redirect('dashboardRecruiterPage')
            else:
                return redirect('dashboardSeekerPage')
    return render(request, 'login.html')

def changePassword(request):
    current = request.user
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        
        if check_password(old_password, current.password):
            if new_password1 == new_password2:
                current.set_password(new_password1)
                current.save()
                update_session_auth_hash(request, current)
                if request.user.user_types == 'recruiter':
                    return redirect('dashboardRecruiterPage')
                else:
                    return redirect('dashboardSeekerPage')
    return render(request, 'change_password.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def homePage(request):
    return render(request, 'index.html')

def dashboardRecruiterPage(request):
    return render(request, 'dashboard_recruiter.html')

def dashboardSeekerPage(request):
    return render(request, 'dashboard_seeker.html')