from django.shortcuts import render,redirect
from portal.models import *
from django.contrib.auth import login,logout,authenticate
from portal.form import *


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

def logoutPage(request):
    logout(request)
    return redirect('loginPage')


def dashboardPage(request):
    
    return render(request, 'dashboard.html')

#________________Teacher_________________

def addTeacherPage(request):
    if request.method == 'POST':
        form = AddTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allTeacherPage')
    else:
        form = AddTeacherForm()

    return render(request, 'teacher/addTeacher.html',{'form':form})

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

def allTeacherPage(request):
    teachers = TeacherModel.objects.all()
    return render(request, 'teacher/allTeacher.html',{'teachers':teachers})


#__________________STUDENT__________________________

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

def studentList(request):
    students = StudentEducationInfoModel.objects.all()
    return render(request, 'student/studentList.html',{'students':students})