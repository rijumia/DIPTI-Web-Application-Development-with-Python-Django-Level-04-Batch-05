from django.shortcuts import render, redirect
from crudApp.models import*

def homePage(request):
    return render(request, 'home.html')

def addPage(request):
    if request.method=='POST':
        user = userModel(
            First_Name = request.POST.get('firstName'),
            Last_Name = request.POST.get('lastName'),
            Age = request.POST.get('age'),
            Email = request.POST.get('email'),
            Address = request.POST.get('address'),
        )
        user.save()
        return redirect('listPage')
    return render(request, 'add.html')

def listPage(request):
    context ={
        'users': userModel.objects.all()
    }
    return render(request, 'list.html', context)

def deletePage(request, myid):
    
    user = userModel.objects.get(id=myid).delete()
    return redirect('listPage')

def updatePage(request, myid):
    context ={
        'user': userModel.objects.get(id=myid)
    }
    if request.method=='POST':
        user = userModel(
            id = myid,
            First_Name = request.POST.get('firstName'),
            Last_Name = request.POST.get('lastName'),
            Age = request.POST.get('age'),
            Email = request.POST.get('email'),
            Address = request.POST.get('address'),
        )
        user.save()
        return redirect('listPage')
    return render(request, 'update.html', context)
    