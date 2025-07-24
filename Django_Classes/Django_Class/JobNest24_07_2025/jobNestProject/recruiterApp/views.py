from django.shortcuts import render,redirect
from recruiterApp.models import *
from recruiterApp.forms import *

# Create your views here.

def recruiterProfile(request):
    return render(request, 'profile_recruiter.html')

def recruiterProfileUpdate(request):
    created = RecruiterProfileModel.objects.get(recruiter_user=request.user)

    if request.method == 'POST':
        form = RecruiterProfileModelForm(request.POST, request.FILES, instance=created)
        if form.is_valid():
            form.save()
            return redirect('recruiterProfile')
    else:
        form = RecruiterProfileModelForm(instance=created)

    return render(request, 'updateProfile.html', {'form': form})

def jobPostPage(request):
    if request.method == 'POST':
        JobTitle = request.POST.get('JobTitle')
        JobDescription = request.POST.get('JobDescription')
        Salary = request.POST.get('Salary')
        Location = request.POST.get('Location')
        deadline = request.POST.get('deadline')
        
        JobModel.objects.create(
            recruiter = request.user.recruiter_profile,
            title = JobTitle,
            description = JobDescription,
            salary = Salary,
            deadline = deadline,
            location = Location,
            job_type = 'Full-Time'
        )
        return redirect('JobList')
    return render(request, 'job_post.html')

def jobList(request):
    return render(request, 'job_list.html')