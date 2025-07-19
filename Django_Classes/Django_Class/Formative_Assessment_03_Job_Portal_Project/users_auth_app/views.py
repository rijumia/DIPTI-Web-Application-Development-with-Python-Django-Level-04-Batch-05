from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout, update_session_auth_hash
from django.contrib.auth.hashers import check_password
from users_auth_app.models import *

# Create your views here.


# def signupPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         user_type = request.POST.get('user_type')

#         if username and phone and user_type:
#             user = CustomUserModel.objects.create_user(
#                 username= username,
#                 email = email,
#                 phone = phone,
#                 password = phone,
#                 user_types = user_type,
#             )
#             if user:
#                 PendingAccountModel.objects.create(
#                     username= username,
#                     email = email,
#                     phone = phone,
#                     user_types = user_type,
#                 )
#                 return redirect('loginPage')

#     return render(request, 'signup.html')

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
                    user_types='Admin',
                )
                return redirect('loginPage')
            else:
                PendingAccountModel.objects.create(
                    username=username,
                    email=email,
                    phone=phone,
                    user_types=user_type,
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
    return render(request, 'changePassword.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')


def profilePage(request):
    return render(request, 'profile.html')

def profileUpdatePage(request):
    user = request.user

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        user.username = username
        user.email = email
        user.phone = phone
        user.save()

        return redirect('profilePage')

    return render(request, 'updateProfile.html')

def dashboardPage(request):
    return render(request, 'dashboard.html')

def pendingList(request):
    pendingUser = PendingAccountModel.objects.all()
    return render(request, 'pendingList.html',{'pendingUser':pendingUser})

def approveUser(request, id):
    if request.method == 'POST':
        pending = PendingAccountModel.objects.get(id=id)
        CustomUserModel.objects.create_user(
            username=pending.username,
            email=pending.email,
            phone=pending.phone,
            password=pending.phone,  
            user_types=pending.user_types,
        )
        pending.delete()
    return redirect('pendingList')


def rejectUser(request, id):
    if request.method == 'POST':
        pending = PendingAccountModel.objects.get(id=id)
        pending.delete()
    return redirect('pendingList')






























    

