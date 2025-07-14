from django.shortcuts import render,redirect
from FormApp.forms import *
from FormApp.models import UserInfoModels

def homePage(request):
    return render(request,'home.html')

def userInfoPage(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST, request.FILES)
        if form.is_valid():
         FullName = form.cleaned_data['FullName']
         email = form.cleaned_data['email']
         phone = form.cleaned_data['phone']
         addrees = form.cleaned_data['addrees']
         image = form.cleaned_data['image']

         UserInfoModels.objects.create(
             FullName=FullName,
             email=email,
             phone=phone,
             addrees=addrees,
             image=image,
             )

         return redirect('homePage')
     
    form = UserInfoForm()
    return render(request,'userInfo.html',{'form':form})


def UserInfoModelView(request):
    if request.method == 'POST':
       formData = UserInfoModelFormTwo(request.POST, request.FILES)
       
       if formData.is_valid():
           formData.save()
           return redirect('homePage')
    else:
        formData = UserInfoModelFormTwo()
    return render(request, 'userModelViiew.html',{'formData':formData})
