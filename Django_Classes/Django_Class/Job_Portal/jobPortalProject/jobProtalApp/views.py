from django.shortcuts import render, redirect, HttpResponse
from jobProtalApp.models import CustomUserModel, JobModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        psw = request.POST.get('psw')
        
        user = authenticate(username=username, password=psw)
        if user:
            login(request, user)
            return redirect('homePage')
    return render(request,'login.html')

def registerPage(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        usertype = request.POST.get('usertype')
        phone = request.POST.get('phone')
        bio = request.POST.get('bio')
        psw = request.POST.get('psw')
        psw_repeat = request.POST.get('psw_repeat')
        
        if psw == psw_repeat:
            user = CustomUserModel.objects.create_user(
                user_type = usertype,
                phone_no = phone,
                bio = bio,
                fullName = fullname,
                username = username,
                password = psw,   
            )
            return redirect('loginPage')
    return render(request,'register.html')

@login_required
def logoutPage(request):
    logout(request)
    return redirect('loginPage')

@login_required
def homePage(request):
    return render(request,'home.html')

@login_required
def profilePage(request):
    return render(request,'profile.html')


@login_required
def jobFeedPage(request):
    feeds = JobModel.objects.all()
    return render(request,'jobFeed.html',{'feeds':feeds})

@login_required
def addJobPage(request):
    if request.method == 'POST':
        logo = request.FILES.get('logo')
        job_title = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        Job_type = request.POST.get('Job_type')
        
        addJob = JobModel.objects.create(
            Created_By = request.user,
            CompanyLogo = logo,
            JobTitle = job_title,
            JobDescription = job_description,
            JopType = Job_type,
        )
        addJob.save()
        return redirect('jobFeedPage')
        
    return render(request,'addJob.html')


