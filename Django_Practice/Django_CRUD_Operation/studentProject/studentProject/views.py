from django.shortcuts import render, redirect
from studentApp.models import*

def homePage(request):
    return render(request, 'home.html')

def addStudentPage(request):

    if request.method == 'POST':

        student_data = studentModel(
            Student_Name = request.POST.get('Student_Name'),
            Student_Roll_No = request.POST.get('Student_roll'),
            Student_Email = request.POST.get('Student_email'),
            Student_Course = request.POST.get('Student_course'),
        )
        student_data.save()
        return redirect('studentListPage')

    return render(request, 'addStudent.html')

def studentListPage(request):
    context = {
        'students': studentModel.objects.all()
    }
    return render(request, 'studentList.html', context)

def deleteStudent(reuest, myid):
    student = studentModel.objects.get(id=myid).delete()
    return redirect('studentListPage')

def updateStudent(request, myid):

    context = {
        'students': studentModel.objects.get(id=myid)
    }
    if request.method == 'POST':

        student_data = studentModel(
            id=myid,
            Student_Name = request.POST.get('Student_Name'),
            Student_Roll_No = request.POST.get('Student_roll'),
            Student_Email = request.POST.get('Student_email'),
            Student_Course = request.POST.get('Student_course'),
        )
        student_data.save()
        return redirect('studentListPage')

    return render(request, 'updateStudent.html', context)

def addTeacherPage(request):

    if request.method == 'POST':
        teacher_data = teacherModel(
            Teacher_Name = request.POST.get('Teacher_Name'),
            Teacher_Email = request.POST.get('Teacher_Email'),
            Teacher_Department = request.POST.get('Teacher_Department'),
            Teacher_Experience = request.POST.get('Teacher_Experience'),
        )
        teacher_data.save()
        return redirect('teacherListPage')
    return render(request, 'addTeacher.html')

def teacherListPage(request):
    context = {
        'teachers': teacherModel.objects.all()
    }
    return render(request, 'teacherList.html', context)

def deleteTeacher(request, myid):
    teacher = teacherModel.objects.get(id=myid).delete()
    return redirect('teacherListPage')

def updateTeacher(request, myid):
    context ={
        'teachers': teacherModel.objects.get(id=myid)
    }
    if request.method == 'POST':
        teacher_data = teacherModel(
            id = myid,
            Teacher_Name = request.POST.get('Teacher_Name'),
            Teacher_Email = request.POST.get('Teacher_Email'),
            Teacher_Department = request.POST.get('Teacher_Department'),
            Teacher_Experience = request.POST.get('Teacher_Experience'),
        )
        teacher_data.save()
        return redirect('teacherListPage')
    return render(request, 'updateTeacher.html', context)

