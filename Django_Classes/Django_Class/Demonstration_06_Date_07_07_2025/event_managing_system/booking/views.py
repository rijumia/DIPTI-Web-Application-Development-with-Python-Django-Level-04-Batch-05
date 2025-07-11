from django.shortcuts import render,redirect
from booking.models import *
from django.contrib.auth import authenticate,login, logout,update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password= password)
        if user:
            login(request, user)
            return redirect('dashboardPage')

    return render(request, 'login.html')

def signupPage(request):
    if request.method == 'POST':
        img = request.FILES.get('img')
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            EventUserModel.objects.create_user(
                username = username,
                full_name = fullname,
                phone_number = phone,
                email = email,
                password = password,
                profile_image = img,
            )
            return redirect('loginPage')
    return render(request, 'signup.html')

@login_required
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
                return redirect('dashboardPage')
    return render(request, 'changepassword.html')

@login_required
def logoutPage(request):
    logout(request)
    return redirect('loginPage')

@login_required
def profilePage(request):

    return render(request, 'profile.html')

@login_required
def dashboardPage(request):
    events = EventBookingModel.objects.all()
    return render(request, 'dashboard.html',{'events':events})

@login_required
def addBookingPage(request):
    if request.method == 'POST':
        event_title = request.POST.get('event_title')
        event_type = request.POST.get('event_type')
        event_description = request.POST.get('event_description')
        event_date = request.POST.get('event_date')
        event_status = request.POST.get('event_status')
        event_location = request.POST.get('event_location')
        
        bookingInfo = EventBookingModel.objects.create(
            event_title= event_title,
            event_type= event_type,
            event_description= event_description,
            event_date= event_date,
            event_status= event_status,
            event_location= event_location,
            create_by = request.user,
        )
        bookingInfo.save()
        return redirect('dashboardPage')
    return render(request, 'addBooking.html')

@login_required
def myBookingPage(request):
    events = EventBookingModel.objects.all()
    return render(request, 'myBooking.html',{'events':events})

@login_required
def changeStatus(request, id):
    status = EventBookingModel.objects.get(id=id)
    if status.event_status == 'NotStarted':
        status.event_status = 'InProgress'
    elif status.event_status == 'InProgress':
        status.event_status = 'Completed'
        
    status.save()
    return redirect('myBookingPage') 

@login_required
def updateBookingPage(request,id):
    upbooking = EventBookingModel.objects.get(id=id)
    if request.method == 'POST':
        upbooking.event_title = request.POST.get('event_title')
        upbooking.event_type = request.POST.get('event_type')
        upbooking.event_description = request.POST.get('event_description')
        upbooking.event_date = request.POST.get('event_date')
        upbooking.event_status = request.POST.get('event_status')
        upbooking.event_location = request.POST.get('event_location')
        upbooking.save()
        return redirect('myBookingPage')
    return render(request, 'updateBooking.html',{'upbooking':upbooking})

@login_required
def deleteBookingPage(request,id):
    booking = EventBookingModel.objects.get(id=id)
    booking.delete()
    return redirect('myBookingPage')

@login_required
def viewBookingPage(request,id):
    booking = EventBookingModel.objects.get(id=id)
    return render(request,'viewBooking.html',{'booking':booking})