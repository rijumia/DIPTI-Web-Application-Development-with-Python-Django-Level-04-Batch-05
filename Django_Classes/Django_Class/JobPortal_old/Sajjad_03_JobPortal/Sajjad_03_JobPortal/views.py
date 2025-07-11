from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from .forms import *
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def signup(request):
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            if user.user_type == 'recruiter':
                RecruiterModel.objects.create(
                    user=user
                )
            elif user.user_type == 'seeker':
                SeekerModel.objects.create(
                    user=user
                )
            return redirect('signin')
    else:
        form=CustomUserForm()
    return render(request,'common/signup.html',{'form':form})

def signin(request):
    if request.method=='POST':
        form=CustomUserAuthForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        form=CustomUserAuthForm()
    return render(request,'common/signin.html',{'form':form})

@login_required
def dashboard(request):
    return render(request,'common/dashboard.html')

@login_required
def logoutpage(request):
    logout(request)
    return redirect('signin')

@login_required
def addjob(request):
    current_user=request.user
    if request.method=="POST":
        form=JobForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.created_by=current_user
            form.save()
            return redirect('joblist')
    else:
        form=JobForm()
    return render(request,'recruiter/addjob.html',{'form':form})

@login_required
def joblist(request):
    jobs=JobModel.objects.all()
    
    jobDict={
        'jobs':jobs
    }
    return render(request,'common/joblist.html',jobDict)

@login_required
def deletejob(request,jobid):
    job=get_object_or_404(JobModel,id=jobid)
    job.delete()
    return redirect('joblist')

@login_required
def editjob(request,jobid):
    job=get_object_or_404(JobModel,id=jobid)
    if request.method=="POST":
        form=JobForm(request.POST,instance=job)
        if form.is_valid():
            form.save()
            return redirect('joblist')
    else:
        form=JobForm(instance=job)
    return render(request,'recruiter/editjob.html',{'form':form})

@login_required
def applyjob(request,jobid):
    # job=JobModel.objects.get(id=jobid)
    current_user=request.user
    job=get_object_or_404(JobModel,id=jobid)
    if request.method=="POST":
        form=JobApplyForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.applied_job=job
            user.applicant=current_user
            user.save()
            return redirect('joblist')
    else:
        form=JobApplyForm()
    return render(request,'seeker/applyjob.html',{'form':form})

@login_required
def baseprofile(request):
    return render(request,'profile/baseprofile.html')

@login_required
def basicinfo(request):
    return render(request,'profile/basicinfo.html')

@login_required
def seekerotherinfo(request):
    user_info=SeekerModel.objects.get(user=request.user)
    return render(request,'profile/seekerotherinfo.html',{'user_info':user_info})

@login_required
def recruiterotherinfo(request):
    return render(request,'profile/recruiterotherinfo.html')

@login_required
def appliedjob(request):
    current_user=request.user
    # applied_job=get_list_or_404(JobApplyModel,applicant=current_user)
    applied_job=JobApplyModel.objects.filter(applicant=current_user)
    return render(request,'seeker/appliedjob.html',{'applied_job':applied_job})

@login_required
def postedjob(request):
    current_user=request.user
    jobs=JobModel.objects.filter(created_by=current_user)
    return render(request,'recruiter/postedjob.html',{'jobs':jobs})

@login_required
def editbasic(request,basicid):
    basic=CustomUserModel.objects.get(id=basicid)
    if request.method=="POST":
        form=CustomUserEditForm(request.POST,instance=basic)
        if form.is_valid():
            form.save()
            return redirect('basicinfo')
    else:
        form=CustomUserEditForm(instance=basic)
    return render(request,'profile/editbasic.html',{'form':form,'basic':basic})

@login_required
def editseekerotherinfo(request,seekerid):
    seeker=SeekerModel.objects.get(id=seekerid)
    if request.method=="POST":
        form=SeekerForm(request.POST,request.FILES,instance=seeker)
        if form.is_valid():
            form.save()
            return redirect('seekerotherinfo')
    else:
        form=SeekerForm(instance=seeker)
    return render(request,'profile/editseekerotherinfo.html',{'form':form,'seeker':seeker})

@login_required
def searchpage(request):
    # search option 
    search=request.GET.get('search')
    # jobs = JobModel.objects.filter(job_title=search)
    jobs = JobModel.objects.filter(
        Q(skill_sets__icontains=search)|
        Q(title__icontains=search)|
        Q(category__icontains=search)|
        Q(created_by__username__icontains=search)
        )
    # change apply button for seeker when already applied 
    job_filtered=[]
    for i in jobs:
        already_applied=JobApplyModel.objects.filter(applicant=request.user,applied_job=i)
        job_filtered.append(
            (i,already_applied),
        )
    jobDict={
        'job_filtered':job_filtered
    }
    return render(request,'common/searchpage.html',jobDict)