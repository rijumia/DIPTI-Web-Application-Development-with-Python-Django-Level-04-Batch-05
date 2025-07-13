from django.shortcuts import render, redirect
from userAuth.models import *
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif CustomUserModel.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            CustomUserModel.objects.create_user(
                username=username,
                email=email,
                password=confirm_password,
                user_type= 'Admin',
            )
            messages.success(request, "Registration successful. Please log in.")
            return redirect('loginPage')

    return render(request, 'signupPage.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'loginPage.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def home(request):
    return render(request, 'home.html')
def profile(request):
    return render(request, 'profile.html')


def registerTeacher(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        teacher_name = request.POST.get('teacher_name')
        teacher_phone = request.POST.get('teacher_phone')
        email = request.POST.get('email')
        teacher_profile = request.FILES.get('teacher_profile')

        teacherData = CustomUserModel.objects.create_user(
            username=username,
            password=teacher_phone,
            email=email,
            user_type = 'Teacher',
        )

        if teacherData:
            TeacherModel.objects.create(
            user_teacher = teacherData,
            teacher_name=teacher_name,
            teacher_phone=teacher_phone,
            teacher_profile=teacher_profile,
        )
        return redirect('teachers')
    return render(request, 'registerTeacher.html')

def teachers(request):
    teacherData = TeacherModel.objects.all()
    return render(request, 'teachers.html', {'teacherInfo': teacherData})



def registerStudent(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        student_name = request.POST.get('student_name')
        student_phone = request.POST.get('student_phone')
        email = request.POST.get('email')
        student_profile = request.FILES.get('student_profile')

        studentData = CustomUserModel.objects.create_user(
            username=username,
            password=student_phone,
            email=email,
            user_type = 'Student',
        )

        if studentData:
            StudentModel.objects.create(
            user_student = studentData,
            student_name=student_name,
            student_phone=student_phone,
            student_profile=student_profile,
        )
        return redirect('students')
    return render(request, 'student/registerStudent.html')

def pendingStudentReg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        student_name = request.POST.get('student_name')
        student_phone = request.POST.get('student_phone')
        email = request.POST.get('email')
        student_profile = request.FILES.get('student_profile')

        PendingStudentModel.objects.create(
        username=username,
        student_name=student_name,
        student_phone=student_phone,
        email=email,
        student_profile=student_profile,
        )
        return redirect('pendingStudentList')
    return render(request, 'student/pendingStudentReg.html')

def pendingStudentList(request):
    pendingStudent = PendingStudentModel.objects.all()
    return render(request, 'student/pendingStudentList.html', {'pendingStudent': pendingStudent})

def acceptPendingStudent(request,id):
    pendingStudent = PendingStudentModel.objects.get(id=id)

    if pendingStudent:
        studentData = CustomUserModel.objects.create_user(
            username=pendingStudent.username,
            password=pendingStudent.student_phone,
            email=pendingStudent.email,
        )

        if studentData:
            StudentModel.objects.create(
            user_student = studentData,
            student_name=pendingStudent.student_name,
            student_phone=pendingStudent.student_phone,
            student_profile=pendingStudent.student_profile,
        )
        pendingStudent.delete()
        return redirect('students')

def students(request):
    studentData = StudentModel.objects.all()
    return render(request, 'student/students.html', {'studentInfo': studentData})