from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from task_App.models import CustomUserModel, TaskModel
from django.contrib.auth.hashers import check_password


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
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        img = request.FILES.get('img')
        bio = request.POST.get('bio')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            CustomUserModel.objects.create_user(
                username = username,
                first_name = fullname,
                email = email,
                profile_picture = img,
                bio = bio,
                password = password,
            )
            return redirect('loginPage')
    return render(request, 'register.html')

@login_required
def logoutPage(request):
    logout(request)
    return redirect('loginPage')

@login_required
def homePage(request):
    tasks = TaskModel.objects.filter(user=request.user)
    in_progress = TaskModel.objects.filter(user=request.user, TaskStatus='in_progress')
    pending = TaskModel.objects.filter(user=request.user, TaskStatus='pending')
    completed = TaskModel.objects.filter(user=request.user, TaskStatus='completed')
    
    return render(request, 'home.html',{'tasks':tasks,'in_progress':in_progress,'pending':pending,'completed':completed})


@login_required
def addTask(request):
    if request.method == 'POST':
        TaskTitle = request.POST.get('TaskTitle')
        TaskDescription = request.POST.get('TaskDescription')
        TaskDueDate = request.POST.get('TaskDueDate')
        TaskPriority = request.POST.get('TaskPriority')
        TaskStatus = request.POST.get('TaskStatus')
        
        task = TaskModel.objects.create(
            user = request.user,
            TaskTitle = TaskTitle,
            TaskDescription = TaskDescription,
            TaskDueDate = TaskDueDate,
            TaskPriority = TaskPriority,
            TaskStatus = TaskStatus,
        )
        return redirect('listTask')
    return render(request, 'addTask.html')

@login_required
def listTask(request):
    tasks = TaskModel.objects.filter(user=request.user)
    return render(request, 'listTask.html',{'tasks':tasks})

@login_required
def updateTask(request, id):
    task = TaskModel.objects.get(id=id)
    if request.method == "POST":
        task.TaskTitle = request.POST.get('TaskTitle')
        task.TaskDescription = request.POST.get('TaskDescription')
        task.TaskDueDate = request.POST.get('TaskDueDate')
        task.TaskPriority = request.POST.get('TaskPriority')
        task.TaskStatus = request.POST.get('TaskStatus')
        task.save()
        return redirect('listTask')

@login_required    
def deleteTask(request, id):
    task = TaskModel.objects.get(id=id)
    task.delete()
    return redirect('listTask')

def changePasswordPage(request):
    
    current_user = request.user
    
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if check_password(old_password, current_user.password):
            if new_password == confirm_password:
                current_user.set_password(new_password)
                current_user.save()
                update_session_auth_hash(request, current_user)
                return redirect('homePage')
    return render(request, 'change_password.html')

def taskDone(request, id):
    task_done = TaskModel.objects.get(id=id)
    task_done.TaskStatus = 'completed'  
    task_done.save()
    return redirect('listTask')

def changeStatus(request, id):
    status = TaskModel.objects.get(id=id)
    
    if status.TaskStatus == 'pending':
        status.TaskStatus = 'in_progress'
    elif status.TaskStatus == 'in_progress':
        status.TaskStatus = 'completed'
        
    status.save()
    return redirect('listTask')

def changePriority(request, id):
    priority = TaskModel.objects.get(id=id)
    
    if priority.TaskPriority == 'low':
        priority.TaskPriority = 'medium'
    elif priority.TaskPriority == 'medium':
        priority.TaskPriority = 'high'
    priority.save()
    return redirect('listTask')

    


