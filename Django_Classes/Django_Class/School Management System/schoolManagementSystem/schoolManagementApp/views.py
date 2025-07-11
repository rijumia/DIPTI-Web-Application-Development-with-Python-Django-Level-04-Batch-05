from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout, update_session_auth_hash
from django.contrib.auth.hashers import check_password
from schoolManagementApp.models import CustomUserModel, TeacherModel, StudentModel

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
    return render(request, 'login.html')

def signupPage(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        hire_date = request.POST.get('hire_date')
        
        
        if password == confirm_password:
            userData = CustomUserModel.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                user_type = user_type,
                password = password,
            )
            userData.save()
            if userData:
                TeacherModel.objects.create(
                    user = userData,
                    subject = subject,
                    phone = phone,
                    hire_date = hire_date,
                )
                return redirect('loginPage')
    return render(request, 'signup.html')

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
    teacherData = None 

    if request.user.user_type == 'teacher':
        teacherData = TeacherModel.objects.get(user=request.user)

    return render(request, 'profile.html', {'teacher': teacherData})


def homePage(request):
    return render(request, 'home.html')

def addStudent(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        enrollment_date = request.POST.get('enrollment_date')
        teacher_instance = TeacherModel.objects.get(user=request.user)
        add = StudentModel.objects.create(
            teacher = teacher_instance,
            first_name = first_name,
            last_name = last_name,
            age = age,
            grade = grade,
            enrollment_date = enrollment_date,
        )
        add.save()
        return redirect('studentList')
    return render(request, 'addStudent.html')

def studentList(request):
    if request.user.username == 'admin':
        studentList = StudentModel.objects.all()
    else:
        try:
            teacher = TeacherModel.objects.get(user=request.user)
            studentList = StudentModel.objects.filter(teacher=teacher)
        except TeacherModel.DoesNotExist:
            studentList = StudentModel.objects.none()
    return render(request, 'studentList.html', {'students': studentList})

