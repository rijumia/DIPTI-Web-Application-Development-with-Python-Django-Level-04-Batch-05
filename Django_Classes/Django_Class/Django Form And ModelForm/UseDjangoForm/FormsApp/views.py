from django.shortcuts import render, redirect
from FormsApp.forms import *
from FormsApp.models import BasicInfoModel

# Create your views here.

def DashboardPage(request):
    return render(request,'dashboard.html')


def BasicInfoView(request):
    if request.method == 'POST':
        form_info = BasicInfoForm(request.POST, request.FILES)

        if form_info.is_valid():
            username = form_info.cleaned_data['username']
            fullName= form_info.cleaned_data['fullName']
            email = form_info.cleaned_data['email']
            addrees = form_info.cleaned_data['addrees']
            profileImage = form_info.cleaned_data['profileImage']

            BasicInfoModel.objects.create(
                username = username,
                fullName = fullName,
                email = email,
                addrees = addrees,
                profileImage = profileImage,
            )
            return redirect('ViewBasicInfo')

    else:
        form_info = BasicInfoForm()
    return render(request,'BasicInfoView.html',{'form_info':form_info})

def BasicInfoModelView(request):
    if request.method == 'POST':
        form_info = BasicInfoModelForm(request.POST, request.FILES)

        if form_info.is_valid():
            form_info.save()
            return redirect('ViewBasicInfo')
    else:
        form_info = BasicInfoModelForm()
    return render(request,'BasicInfoModelView.html',{'form_info':form_info})

def ViewBasicInfo(request):
    basic_info = BasicInfoModel.objects.all()
    return render(request,'ViewBasicInfo.html',{'basic_info':basic_info})

def updateBasicInfo(request, id):
    basic_info = BasicInfoModel.objects.get(id=id)

    if request.method == 'POST':
        form_info = BasicInfoModelForm(request.POST,request.FILES, instance=basic_info)
        if form_info.is_valid():
            form_info.save()
            return redirect('ViewBasicInfo')
    else:
        form_info = BasicInfoModelForm(instance=basic_info)
    
    return render(request,'updateBasicInfo.html',{'form_info':form_info})