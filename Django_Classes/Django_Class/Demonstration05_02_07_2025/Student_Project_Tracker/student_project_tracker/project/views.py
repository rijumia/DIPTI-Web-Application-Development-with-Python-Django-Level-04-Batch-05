from django.shortcuts import render, redirect
from project.models import *
from django.contrib.auth import authenticate, login, logout


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username,password=password)
        if user:
            login(request, user)
            return redirect('homePage')
    return render(request, 'login.html')

def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        studentname = request.POST.get('studentname')
        studentid = request.POST.get('studentid')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            userData = CustomUserModel.objects.create_user(
            username = username,
            email = email,
            password = password,
           )
            userData.save()
            if userData:
                StudentModel.objects.create(
                    user = userData,
                    studentName = studentname,
                    studentId = studentid,
                )
                return redirect('loginPage')
    return render(request, 'register.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def homePage(request):
    user = request.user
    if user.is_staff or user.is_superuser:
        projectData = ProjectModel.objects.all()
    else:
        projectData = ProjectModel.objects.filter(user = request.user)
    return render(request, 'home.html',{'projects':projectData})

def addPage(request):
    if request.method == 'POST':
        projectName = request.POST.get('projectName')
        projectDescription = request.POST.get('projectDescription')
        projectStatus = request.POST.get('projectStatus')
        deadline = request.POST.get('deadline')
        createdBy = request.POST.get('createdBy')
        updatedAt = request.POST.get('updatedAt')
        
        addData = ProjectModel.objects.create(
            user = request.user,
            project_name = projectName,
            project_description = projectDescription,
            project_status = projectStatus,
            deadline = deadline,
            created_by = createdBy,
            updated_at = updatedAt,
        )
        addData.save()
        return redirect('listPage')
    return render(request, 'add_project.html')

def updatePage(request,id):
    updatedata = ProjectModel.objects.get(id=id)
    if request.method == 'POST':
        updatedata.project_name = request.POST.get('projectName')
        updatedata.project_description = request.POST.get('projectDescription')
        updatedata.project_status = request.POST.get('projectStatus')
        updatedata.deadline = request.POST.get('deadline')
        updatedata.save()
        
        return redirect('listPage')
    return render(request, 'update_project.html',{'updatedata':updatedata})

def listPage(request):
    projectData = ProjectModel.objects.filter(user = request.user)
    return render(request, 'project_list.html',{'projectData':projectData})

def viewPage(request, id):
    project = ProjectModel.objects.get(id=id)
    return render(request, 'project_view.html',{'project':project})

def deletePage(request, id):
    projectData = ProjectModel.objects.filter(id=id)
    projectData.delete()
    
    return redirect('listPage')

def changeStatus(request, id):
    status = ProjectModel.objects.get(id=id)
    if status.project_status == 'NotStarted':
        status.project_status = 'InProgress'
    elif status.project_status == 'InProgress':
        status.project_status = 'Completed'
        
    status.save()
    return redirect('listPage') 

    

