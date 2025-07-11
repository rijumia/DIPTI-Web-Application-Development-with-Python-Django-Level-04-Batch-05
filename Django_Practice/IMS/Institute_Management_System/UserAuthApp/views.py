from django.shortcuts import render, redirect
from UserAuthApp.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('registerPage')

        if CustomUserModel.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('registerPage')

        if CustomUserModel.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('registerPage')

        user = CustomUserModel.objects.create_user(
            username=username, 
            email=email, 
            password=password1,
            user_type = 'Admin',
            )
        user.save()
        messages.success(request, "Account created successfully.")
        return redirect('loginPage')  

    return render(request, 'register.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('homePage')  # or wherever you want
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('loginPage')

    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')


def changePasswordPage(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        user = request.user

        # Check old password
        if not user.check_password(old_password):
            messages.error(request, 'Current password is incorrect.')
            return redirect('changePassword')

        # Check new password match
        if new_password1 != new_password2:
            messages.error(request, 'New passwords do not match.')
            return redirect('changePassword')

        # Optional: Add validation (e.g. min length)
        if len(new_password1) < 6:
            messages.error(request, 'New password must be at least 6 characters long.')
            return redirect('changePassword')

        # All good – change password
        user.set_password(new_password1)
        user.save()
        update_session_auth_hash(request, user)  # Keep user logged in
        messages.success(request, 'Your password has been changed successfully.')
        return redirect('homePage')

    return render(request, 'changePassword.html')

def profileInfoPage(request):
    return render(request, 'profileInfo.html')



def homePage(request):
    return render(request, 'home.html')


def registerTeacherPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        teacher_name = request.POST.get('teacher_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        profile_picture = request.FILES.get('profile_picture')


        if CustomUserModel.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('registerTeacherPage')
        if CustomUserModel.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('registerTeacherPage')

 
        teacherData = CustomUserModel.objects.create_user(
            username=username,
            password=phone, 
            email=email,
            user_type = 'Teacher',
            )
        if teacherData:
            TeacherModel.objects.create(
                teacher_user = teacherData,
                teacher_name = teacher_name,
                teacher_profile =profile_picture,
                teacher_phone = phone,
            )
        
        messages.success(request, "Teacher registered successfully.")
        return redirect('teacherListPage')

    return render(request, 'teacher.html')

def teacherListPage(request):
    teacherInfo = TeacherModel.objects.all()
    return render(request, 'teacherList.html',{'teacherInfo':teacherInfo})


def registerStudentPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        Student_name = request.POST.get('Student_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        profile_picture = request.FILES.get('profile_picture')


        if CustomUserModel.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('registerTeacherPage')
        if CustomUserModel.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('registerTeacherPage')

 
        studentData = CustomUserModel.objects.create_user(
            username=username,
            password=phone, 
            email=email,
            user_type = 'Student',
            )
        if studentData:
            StudentModel.objects.create(
                student_user = studentData,
                student_name = Student_name,
                student_profile =profile_picture,
                student_phone = phone,
            )
        
        messages.success(request, "Student registered successfully.")
        return redirect('studentListPage')

    return render(request, 'registerStudent.html')

def studentListPage(request):
    studentInfo = StudentModel.objects.all()
    return render(request, 'studentList.html',{'studentInfo':studentInfo})

