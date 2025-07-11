from django.shortcuts import render, redirect
from tasksApp.models import*

def homePage(request):
    return render(request, 'home.html')

def addPage(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        created_at = request.POST.get('created_at')

        task = taskModel(
            Title=title, 
            Description=description, 
            Status=status, 
            DueDate=due_date, 
            CreatedAt=created_at
            )
        task.save()
        return redirect('listPage')
    return render(request, 'addTask.html')


def listPage(request):
    context={
        'lists': taskModel.objects.all()
    }
    return render(request, 'taskList.html', context)

def deleteTaskPage(request, id):
    task = taskModel.objects.get(id=id)
    task.delete()
    return redirect('listPage')

def updateTaskPage(request, id):
    task = taskModel.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        created_at = request.POST.get('created_at')

        task.Title = title
        task.Description = description
        task.Status = status
        task.DueDate = due_date
        task.CreatedAt = created_at
        task.save()
        return redirect('listPage')
    return render(request, 'updateTask.html', {'task': task})

def viewPage(request, id):
    task = taskModel.objects.get(id=id)
    # context={
    #     'data':task
    # }
    return render(request, 'viewTask.html', {'task': task})