from django.shortcuts import render, redirect
from myApp.models import *

def homePage(request):
    return render(request, 'home.html')

def contactPage(request):
    return render(request, 'contact.html')
def loginPage(request):
    return render(request, 'login.html')

def workPage(request):
    return render(request, 'work.html')

def aboutPage(request):
    return render(request, 'about.html')

def signupPage(request):
    return render(request, 'signup.html')

def viewStudentPage(request):

    studentData = studentModel.objects.all()

    context = {
        'students': studentData,
    }

    return render(request, 'viewStudent.html', context)


def coursePage(request):
    courseData = courseModel.objects.all()

    context = {
        'courses': courseData,
    }

    return render(request, 'viewCourse.html', context)