from django.shortcuts import render,redirect
from portal.models import *
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from portal.form import *
import random
from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboardPage')
    return render(request, 'login.html')

def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            user = CustomUserModel.objects.create_user(
                username = username,
                email = email,
                password = password,
                user_type = 'Admin',
            )
            user.save()
            return redirect('loginPage')
    return render(request, 'signup.html')

@login_required
def changePasswordPage(request):
    if request.method == 'POST':
        oldPassword = request.POST.get('oldPassword')
        newPassword1 = request.POST.get('newPassword1')
        newPassword2 = request.POST.get('newPassword2')
        
        current_user = request.user
        
        if check_password(oldPassword, current_user.password):
            if newPassword1 == newPassword2:
                current_user.set_password(newPassword1)
                current_user.save()
                update_session_auth_hash(request, current_user)
                return redirect('dashboardPage')
        
    return render(request, 'master/changePassword.html')

@login_required
def logoutPage(request):
    logout(request)
    return redirect('loginPage')



@login_required
def dashboardPage(request):
    
    return render(request, 'dashboard.html')

#________________Teacher_________________

@login_required
def addTeacherPage(request):
    if request.method == 'POST':
        form = AddTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allTeacherPage')
    else:
        form = AddTeacherForm()

    return render(request, 'teacher/addTeacher.html',{'form':form})

@login_required
def updateTeacherPage(request,id):
    teacher = TeacherModel.objects.get(id=id)
    if request.method == 'POST':
        form = AddTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('allTeacherPage')
    else:
        form = AddTeacherForm(instance=teacher)
    return render(request, 'teacher/updateTeacher.html',{'form':form})

@login_required
def allTeacherPage(request):
    teachers = TeacherModel.objects.all()
    return render(request, 'teacher/allTeacher.html',{'teachers':teachers})


#__________________STUDENT__________________________

@login_required
def addStudentPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        degreeName = request.POST.get('degreeName')
        grade = request.POST.get('grade')
        passingYear = request.POST.get('passingYear')
        
        student_info = StudentBasicInfoModel.objects.create(
            name = name,
            email = email,
            address = address,
        )
        
        if student_info:
            StudentEducationInfoModel.objects.create(
                student = student_info,
                degreeName = degreeName,
                grade = grade,
                passingYear = passingYear,
            )
            return redirect('studentList')
    return render(request, 'student/addStudent.html')

@login_required
def studentList(request):
    students = StudentEducationInfoModel.objects.all()
    return render(request, 'student/studentList.html',{'students':students})

#________________Forgot Password__________________________

def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        user = CustomUserModel.objects.filter(email=email).exists()
        if user:
            otp = random.randint(100000, 999999)
            cache.set(email, otp, timeout=500)
            send_mail(
                "Forgot Password OTP",
                f"Your Otp is :{otp}",
                settings.EMAIL_HOST_USER,
                [email],
            )
            request.session['reset_email'] = email
            return redirect('verifyOtp')
    return render(request, 'forgot_password/forgotPassword.html')

def verifyOtp(request):
    email = request.session.get('reset_email')
    if request.method == 'POST':
        mail_otp = request.POST.get('otp_mail')
        
        send_otp = cache.get(email)
        
        if mail_otp == str(send_otp):
            cache.set(email, True, timeout=120)
            
            return redirect('resetPassword')
            
    return render(request, 'forgot_password/verifyOtp.html')

def resetPassword(request):
    email = request.session.get('reset_email')
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')
        
        otp_verify = cache.get(email)
        
        if otp_verify:
            if new_password == confirm_new_password:
                user_data = CustomUserModel.objects.get(email=email)
                user_data.set_password(new_password)
                user_data.save()
                del request.session['reset_email']

                return redirect('loginPage')
            
    return render(request, 'forgot_password/resetPassword.html')