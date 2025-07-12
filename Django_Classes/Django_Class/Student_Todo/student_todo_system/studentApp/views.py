from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from studentApp.models import studentModel, todoModel

@login_required
def homePage(request):
    todolist = todoModel.objects.all()
    return render(request, 'home.html',{'todolist': todolist})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('homePage')
        else:
            return HttpResponse('Somthing Is Wrong!!')

    return render(request, 'login.html')
def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('loginPage')
        else:
            return HttpResponse('password and confirm_password not same!!!')
    return render(request, 'register.html')
@login_required
def logoutPage(request):
    logout(request)
    return redirect('loginPage')

@login_required
def addStudent(request):
    if request.method == 'POST':
        studentName = request.POST.get('studentName')
        studentRoll = request.POST.get('studentRoll')
        studentDepartment = request.POST.get('studentDepartment')
        studentImage = request.FILES.get('studentImage')
        
        studentinfo = studentModel(
            StudentName = studentName,
            StudentRoll = studentRoll,
            StudentDepartment = studentDepartment,
            StudentImage = studentImage,
        )
        studentinfo.save()
        return redirect('studentList')
    return render(request, 'add_student.html')

@login_required
def studentUpdate(request,id):
    student = studentModel.objects.get(id=id)
    if request.method == 'POST':
        id = id
        student.StudentName = request.POST.get('studentName')
        student.StudentRoll = request.POST.get('studentRoll')
        student.StudentDepartment = request.POST.get('studentDepartment')
        if request.FILES.get('studentImage'):
            student.StudentImage = request.FILES.get('studentImage')
        student.save()
        return redirect('studentList')
    return render(request, 'update_student.html', {'student': student})

@login_required
def studentList(request):
    students = studentModel.objects.all()
    return render(request, 'student_list.html', {'students': students})

@login_required
def studentView(request, id):
    students = studentModel.objects.get(id=id)
    return render(request, 'view_student.html', {'students': students})

@login_required
def studentDelete(request, id):
    student = studentModel.objects.get(id=id)
    student.delete()
    return redirect('studentList')

@login_required
def addTask(request):
    if request.method == 'POST':
        todoTitle = request.POST.get('todoTitle')
        todoDescription = request.POST.get('todoDescription')
        todoStatus = request.POST.get('todoStatus')
        todoDueDate = request.POST.get('todoDueDate')
        
        todotinfo = todoModel(
            TodoTitle = todoTitle,
            TodoDescription = todoDescription,
            TodoStatus = todoStatus,
            TodoDueDate = todoDueDate,
        )
        todotinfo.save()
        return redirect('homePage')
    return render(request, 'add_task.html')

@login_required
def taskUpdate(request,id):
    task = todoModel.objects.get(id=id)
    if request.method == 'POST':
        task.TodoTitle = request.POST.get('todoTitle')
        task.TodoDescription = request.POST.get('todoDescription')
        task.TodoStatus = request.POST.get('todoStatus')
        task.TodoDueDate = request.POST.get('todoDueDate')
        task.save()
        return redirect('homePage')
    return render(request, 'update_task.html', {'task': task})

# def studentView(request, id):
#     students = studentModel.objects.get(id=id)
#     return render(request, 'view_student.html', {'students': students})
@login_required
def taskDelete(request, id):
    task = todoModel.objects.get(id=id)
    task.delete()
    return redirect('homePage')
