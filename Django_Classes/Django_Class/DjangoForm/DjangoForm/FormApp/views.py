from django.shortcuts import render,redirect
from FormApp.forms import *
from FormApp.models import UserInfoModels

def homePage(request):
    return render(request,'home.html')

def userInfoPage(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
         FullName = form.cleaned_data['FullName']
         email = form.cleaned_data['email']
         phone = form.cleaned_data['phone']
         addrees = form.cleaned_data['addrees']

         UserInfoModels.objects.create(
             FullName=FullName,
             email=email,
             phone=phone,
             addrees=addrees
             )

         return redirect('homePage')
     
    form = UserInfoForm()
    return render(request,'userInfo.html',{'form':form})
