from django.shortcuts import render,redirect
from employer_app.models import *
from employer_app.forms import *
from candidate_app.models import *
from django.contrib import messages

# Create your views here.


# def createJobPage(request):
#     employer_profile = EmployerProfileModel.objects.get(employer_user=request.user)

#     if request.method == 'POST':
#         JobModel.objects.create(
#             employer=employer_profile,
#             title=request.POST.get('title'),
#             description=request.POST.get('description'),
#             requirements=request.POST.get('requirements'),
#             salary=request.POST.get('salary'),
#             job_type=request.POST.get('job_type'),
#             deadline=request.POST.get('deadline')
#         )
#         return redirect('dashboardPage')

#     return render(request, 'createJob.html')
def createJobPage(request):
    if request.method == 'POST':
        formData = JobModelForm(request.POST)

        employer_data = EmployerProfileModel.objects.get(employer_user= request.user)
        if formData.is_valid():
            job_formData = formData.save(commit=False)
            job_formData.employer = employer_data
            formData.save()
            return redirect('jobListPage')
    else:
        formData = JobModelForm()
    return render(request, 'createJob.html',{'formData':formData})

def jobListPage(request):
    employer_data = EmployerProfileModel.objects.get(employer_user= request.user)
    jobs = JobModel.objects.filter(employer = employer_data)
    return render(request, 'jobList.html',{'jobs':jobs})



def updateJobPage(request, id):
    jobData = JobModel.objects.get(id=id)
    if request.method == 'POST':
        formData = JobModelForm(request.POST,instance=jobData)
        if formData.is_valid():
            formData.save()
            return redirect('jobListPage')
    else:
        formData = JobModelForm(instance=jobData)
    return render(request, 'updateJob.html',{'formData':formData})

def deleteJobPage(request, id):
    JobModel.objects.get(id=id).delete()
    return redirect('jobListPage')

def jobDetailsPage(request, id):
    job = JobModel.objects.get(id=id)
    return render(request, 'jobDetails.html',{'job':job})



def allJobApplicationsPage(request):
    employer = request.user
    jobs = JobModel.objects.filter(employer__employer_user=employer)
    applications = JobApplicationModel.objects.filter(job__in=jobs).select_related('job', 'candidate')

    return render(request, 'jobApplications.html', {
        'applications': applications,
    })

def changeApplicationStatusPage(request, id):
    status = JobApplicationModel.objects.get(id=id)
    if status.status == 'Applied':
        status.status = 'Interview'
    elif status.status == 'Interview':
        status.status = 'Offered'
    else:
        status.status = 'Rejected'   
    status.save()
    return redirect('allJobApplicationsPage')