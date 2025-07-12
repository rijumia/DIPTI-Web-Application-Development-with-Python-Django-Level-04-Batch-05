from django.shortcuts import render, redirect
from myApp.models import personalInfoModel


def home(request, id):
    info = personalInfoModel.objects.get(id=id)
    return render(request, 'home.html', {'info': info})

def createPage(request):
    if request.method == 'POST':
        profile = request.FILES.get('profile_pic')
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        info = personalInfoModel(
            Profile = profile,
            Name = name,
            Phone = phone,
        )
        info.save()
        return redirect('readPage')
    return render(request, 'create.html')

def readPage(request):
    info = personalInfoModel.objects.all()
    return render(request, 'read.html',{'info': info})

def updatePage(request, id):
    info = personalInfoModel.objects.get(id=id)
    if request.method == 'POST':
        info.Name = request.POST.get('name')
        info.Phone = request.POST.get('phone')
        if request.FILES.get('profile_pic'):
            info.Profile = request.FILES.get('profile_pic')
        
        info.save()
        return redirect('readPage')
    return render(request, 'update.html', {'info': info})

def deletePage(request, id):
    infoDelete = personalInfoModel.objects.get(id=id)
    infoDelete.delete()
    return redirect('readPage')