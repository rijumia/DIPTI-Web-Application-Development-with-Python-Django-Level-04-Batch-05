from django.shortcuts import render
from CourseApp.models import *

def createCoursePage(request):

    return render(request, 'courses/createCourse.html')
