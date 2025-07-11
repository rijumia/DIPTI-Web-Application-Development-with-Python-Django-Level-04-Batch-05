from django.shortcuts import render, redirect
from studentApp.models import *

def homePage(request):
    return render(request, 'home.html')

def studentListPage(request):

    context ={
        'students': studentModel.objects.all()
    }
    return render(request, 'studentList.html', context)

def addStudentPage(request):

    if request.method == 'POST':

        newstudent = studentModel(
            StudentName = request.POST['studentname'],
            StudentAddress = request.POST['studentaddress'],
            StudentDepartment = request.POST['studentdepartment'],
            StudentAge = request.POST['studentage']
        )
        newstudent.save()
        return redirect('studentListPage')
    return render(request, 'addStudent.html')