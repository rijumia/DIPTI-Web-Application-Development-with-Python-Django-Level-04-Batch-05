from django.shortcuts import render,redirect

from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def signupPage(request):
    
    if request.method=='POST':
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        Confirm_password=request.POST.get("Confirm_password")
        user_type=request.POST.get("user_type")
        Profile_Pic=request.FILES.get("Profile_Pic")
    
        
        if password==Confirm_password:
            
            
            user=customUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_type=user_type,
                Profile_Pic=Profile_Pic,
            )
            if user_type=='seeker':
                seekerProfileModel.objects.create(user=user)
                
            elif user_type=='recruiter':
                recruiterProfileModel.objects.create(user=user)
            
            return redirect("signInPage")
            
    return render(request,"signupPage.html")


def signInPage(request):
    if request.method == 'POST':
        
        user_name=request.POST.get("username")
        pass_word=request.POST.get("password")

        try:
            user = authenticate(request, username=user_name, password=pass_word)

            if user is not None:
                login(request, user)
                return redirect('homePage') 
            else:
                return redirect('signInPage')

        except customUser.DoesNotExist:
            return redirect('signInPage')

    return render(request, 'signInPage.html')

@login_required
def homePage(request):
    
    
    return render(request,"homePage.html")


def logoutPage(request):
    
    logout(request)
    
    return redirect('signInPage')

@login_required
def profilePage(request):
    
    return render(request,"profilePage.html")



@login_required
def createdJob(request):
    
    jobs=JobModel.objects.filter(user=request.user)
    
    context={
        'jobs':jobs
    }
    return render(request,"createdJob.html",context)

def deleteJob(request,job_id):
    
    jobs=JobModel.objects.get(id=job_id).delete()
    
    return redirect("createdJob")

def editJob(request,job_id):
    
    jobs=JobModel.objects.get(id=job_id)
    context={
        'jobs':jobs
    }
    
    if request.method=='POST':
        
        j_id=request.POST.get("j_id")
        job_title=request.POST.get("job_title")
        vacancy=request.POST.get("vacancy")
        skill=request.POST.get("skill")
        Job_Image=request.FILES.get("Job_Image")
        description=request.POST.get("description")
        category=request.POST.get("category")
        
        job=JobModel(
            id=j_id,
            user=request.user,
            title=job_title,
            openings=vacancy,
            skills=skill,
            Job_Image=Job_Image,
            description=description,
            category=category
        )
        job.save()
        
        return redirect("createdJob")
    
    return render(request,"editJob.html",context)


def viewJob(request,job_id):
    
    jobs=JobModel.objects.get(id=job_id)
    context={
        'jobs':jobs
    }
    
    return render(request,"viewJob.html",context)



def applyJob(request,job_id):
    
    jobs=JobModel.objects.get(id=job_id)
    context={
        'jobs':jobs
    }
    
    
    if request.method=='POST':
        
        skill=request.POST.get("skill")
        Cover=request.POST.get("Cover")
        apply_Image=request.FILES.get("apply_Image")
        resume=request.FILES.get("resume")
        
        apply=jobApplyModel(
            user=request.user,
            job=jobs,
            Skills=skill,
            Cover=Cover,
            Resume=resume,
            Apply_Image=apply_Image,
        )
        
        apply.save()
        
        return redirect("jobFeed")
        
    return render(request,"applyJob.html",context)



def jobFeed(request):
    jobs = JobModel.objects.all()
    
    for job in jobs:
        job.skill_list = job.skills.split(",") if job.skills else []
    
    context = {
        'jobs': jobs
    }
    return render(request,"jobFeed.html",context)


def skillMatchingPage(request):
    
    # user=request.user
    
    # mySkill=user.seekerProfile.skills
    # jobs=JobModel.objects.filter(skills=mySkill)
    # context={
    #     'jobs':jobs
    # }
    # print(mySkill)
    user = request.user

    if user.user_type == "seeker":
        # Split seeker skills
        seeker_skills = [s.strip().lower() for s in user.seekerProfile.skills.split(",")] if user.seekerProfile.skills else []
        
        # Jobs matching any skill
        jobs = JobModel.objects.filter(
            Q(skills__icontains=seeker_skills[0]) |
            Q(skills__icontains=",".join(seeker_skills))
        ) if seeker_skills else []

        # Clean up skills list for template
        for job in jobs:
            job.skill_list = [s.strip() for s in job.skills.split(",")] if job.skills else []

        context = {
            "role": "seeker",
            "jobs": jobs,
            "mySkills": seeker_skills,
        }

    elif user.user_type == "recruiter":
        # Recruiter’s jobs
        jobs = JobModel.objects.filter(user=user)

        matches = []
        for job in jobs:
            job_skills = [s.strip().lower() for s in job.skills.split(",")] if job.skills else []
            seekers = seekerProfileModel.objects.filter(
                skills__iregex=r'(' + '|'.join(job_skills) + ')'
            ) if job_skills else []
            matches.append({
                "job": job,
                "seekers": seekers
            })

        context = {
            "role": "recruiter",
            "matches": matches,
        }
    
    return render(request,"skillMatchingPage.html",context)


def addJob(request):
    
    if request.method=='POST':
        
        job_title=request.POST.get("job_title")
        vacancy=request.POST.get("vacancy")
        skill=request.POST.get("skill")
        Job_Image=request.FILES.get("Job_Image")
        description=request.POST.get("description")
        category=request.POST.get("category")
        
        job=JobModel(
            user=request.user,
            title=job_title,
            openings=vacancy,
            skills=skill,
            Job_Image=Job_Image,
            description=description,
            category=category
        )
        job.save()
        
        return redirect("createdJob")
    
    
    return render(request,"addJob.html")
  


def searchJob(request):
    query = request.GET.get('query')
    
    jobs = JobModel.objects.filter(
        Q(title__icontains=query) |
        Q(category__icontains=query) |
        Q(skills__icontains=query)
    )

    for job in jobs:
        job.skill_list = job.skills.split(",") if job.skills else []
    
    context = {
        'query': query,
        'jobs': jobs
    }
    return render(request,"search.html",context)


@login_required
def editProfile(request):
    

        
    return render(request,"editProfile.html")



