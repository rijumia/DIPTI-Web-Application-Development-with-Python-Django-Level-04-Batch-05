from django.shortcuts import render
from CourseApp.models import *

def createCoursePage(request):
    return render(request, 'CourseApp/courses/create_course.html')

def coursePage(request):
    return render(request, 'courses/course.html')
