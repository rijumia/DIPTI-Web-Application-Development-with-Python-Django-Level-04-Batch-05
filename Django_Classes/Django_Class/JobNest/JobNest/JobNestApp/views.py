from django.shortcuts import render,redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate, update_session_auth_hash
from django.contrib.auth.hashers import check_password
from JobNestApp.models import *
from JobNestApp.forms import CreateJobModelForm

# Create your views here.
def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user_types = request.POST.get('user_types')
        
        if password1 == password2:
            user_create = CustomUserModel.objects.create_user(
                username = username,
                email = email,
                phone = phone,
                password = password1,
                user_types = user_types,
            )
            return redirect('loginPage')
        else:
            messages.error(request, 'Password and Confirm Not Macth')
            
    return render(request, 'signup.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username =username, password =password)
        if user:
            login(request, user)
            return redirect('dashboardPage')
        else:
            messages.warning(request, 'Username Or Password Not Right')
    return render(request, 'login.html')

def changePassword(request):
    
    current_user = request.user
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        
        if check_password(old_password, current_user.password):
            if new_password1 == new_password2:
                current_user.set_password(new_password1)
                current_user.save()
                update_session_auth_hash(request, current_user)
                return redirect('dashboardPage')
    return render(request, 'changePassword.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')


def dashboardPage(request):
    return render(request, 'dashboard.html')

def profilePage(request):
    return render(request, 'profile.html')

def updateProfilePage(request):
    
    return render(request, 'updateProfile.html')
    


def createJobPage(request):
    if request.method == 'POST':
        form = CreateJobModelForm(request.POST)

        recruiter_profile = RecruiterProfile.objects.get(user= request.user)
        if form.is_valid():
            job = form.save(commit=False) 
            job.recruiter = recruiter_profile
            job.save() 
            return redirect('jobList') 
    else:
        form = CreateJobModelForm()
    return render(request, 'createJob.html', {'form': form})



def jobListPage(request):
    job_data = CreateJobModel.objects.filter(recruiter__user=request.user)
    return render(request, 'jobList.html',{'job_data':job_data})