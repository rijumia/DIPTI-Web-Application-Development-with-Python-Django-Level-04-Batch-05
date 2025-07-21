from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout, update_session_auth_hash
from django.contrib.auth.hashers import check_password
from users_auth_app.models import *
from employer_app.models import EmployerProfileModel
from candidate_app.models import CandidateProfileModel
from django.contrib import messages

# Create your views here.


def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        user_type = request.POST.get('user_type')

        if username and phone and user_type:
            if user_type == 'Admin':
                user = CustomUserModel.objects.create_user(
                    username=username,
                    email=email,
                    phone=phone,
                    password=phone,
                    user_types= user_type,
                )
                return redirect('loginPage')
            else:
                PendingAccountModel.objects.create(
                    username=username,
                    email=email,
                    phone=phone,
                    user_types=user_type,
                    pending_status = 'Pending',
                )
                return redirect('loginPage')

    return render(request, 'signup.html')



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.user_types == 'Admin':
                login(request, user)
                return redirect('pendingList')
            else:
                login(request, user)
                return redirect('dashboardPage')
        else:
            messages.error(request, 'User Don\'t Exist')
    return render(request, 'login.html')

def changePasswordPage(request):
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
                return redirect('homePage')
            messages.error(request, 'New Password and Confim New Password Not Macth')
        
    return render(request, 'changePassword.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')


def profilePage(request):
    return render(request, 'profile.html')

def profileUpdatePage(request, id):
    
    if request.user.user_types == 'Employer':
        
        em_profile_data = EmployerProfileModel.objects.get(id=id)
        if request.method == 'POST':
            em_profile_data.company_name = request.POST.get('company_name')
            em_profile_data.email = request.POST.get('email')
            em_profile_data.phone = request.POST.get('phone')
            em_profile_data.location = request.POST.get('location')
            em_profile_data.about_company = request.POST.get('about')
            img = request.FILES.get('logo')
            if img:
                em_profile_data.company_logo = img
            em_profile_data.save()
            return redirect('profilePage')
        
    if request.user.user_types == 'Candidate':  
        
        ca_profile_data = CandidateProfileModel.objects.get(id=id)  

    return render(request, 'updateProfile.html',{'em_profile_data':em_profile_data})

def dashboardPage(request):
    return render(request, 'dashboard.html')

def pendingList(request):
    pendingUser = PendingAccountModel.objects.all()
    return render(request, 'pendingList.html',{'pendingUser':pendingUser})

def approveUser(request, id):

    pending = PendingAccountModel.objects.get(id=id)
    if pending:
        userData = CustomUserModel.objects.create_user(
            username=pending.username,
            email=pending.email,
            phone=pending.phone,
            password=pending.phone,  
            user_types=pending.user_types,
        )
        
        if userData:
            if pending.user_types == 'Employer':
                EmployerProfileModel.objects.create(
                    employer_user=userData,
                    email=pending.email,
                    phone=pending.phone,
                )
            elif pending.user_types == 'Candidate':
                CandidateProfileModel.objects.create(
                    candidate_user=userData,
                    email=pending.email,
                    phone=pending.phone,  
                )
        pending.delete()       
    return redirect('pendingList')


def rejectUser(request, id):
    pending = PendingAccountModel.objects.get(id=id)
    pending.pending_status = 'Rejected'
    pending.save() 
    return redirect('pendingList')






























    

