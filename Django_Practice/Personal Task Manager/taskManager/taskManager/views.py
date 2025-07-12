from django.shortcuts import render, redirect
from taskApp.models import*

def homePage(request):
    return render(request, 'home.html')

def addTaskPage(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        completed = request.POST.get('completed') == 'on'

        task = TaskModel(
            title=title,
            category=category,
            description=description,
            deadline=deadline,
            completed=completed
        )
        task.save()
        return redirect('taskListPage')
    return render(request, 'addTask.html')

def taskListPage(request):
    list={
        'tasks': TaskModel.objects.all()
    }
    return render(request, 'taskList.html', list)

def deleteTask(request, id):
    task = TaskModel.objects.get(id=id).delete()
    return redirect('taskListPage')

def updateTask(request, id):
    task = TaskModel.objects.get(id=id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.category = request.POST.get('category')
        task.description = request.POST.get('description')
        task.deadline = request.POST.get('deadline')
        task.completed = request.POST.get('completed') == 'on'
        task.save()
        return redirect('taskListPage')
    return render(request, 'updateTask.html', {'task': task})

def taskDetail(request, id):
    task = TaskModel.objects.get(id=id)
    return render(request, 'taskDetail.html', {'task': task})