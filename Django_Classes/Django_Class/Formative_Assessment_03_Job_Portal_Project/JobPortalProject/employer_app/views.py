from django.shortcuts import render,redirect
from employer_app.models import *

# Create your views here.
def employerProfile(request):
    employerInfo = EmployerProfileModel.objects.all()
    return render(request, 'employerProfile.html',{'employerInfo':employerInfo})


def createJobPage(request):
    employer_profile = EmployerProfileModel.objects.get(employer_user=request.user)

    if request.method == 'POST':
        JobModel.objects.create(
            employer=employer_profile,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            requirements=request.POST.get('requirements'),
            salary=request.POST.get('salary'),
            job_type=request.POST.get('job_type'),
            deadline=request.POST.get('deadline')
        )
        return redirect('dashboardPage')

    return render(request, 'createJob.html')