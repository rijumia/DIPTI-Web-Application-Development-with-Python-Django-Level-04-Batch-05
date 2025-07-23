from django.shortcuts import render,redirect
from candidate_app.models import*
from candidate_app.forms import*

# Create your views here.
def appliedJobList(request):
    candidate_data = CandidateProfileModel.objects.get(candidate_user= request.user)
    apply_data = JobApplicationModel.objects.filter(candidate=candidate_data)
    return render(request, 'applied_job_list.html',{'apply_data':apply_data})

def applyJob(request, id):
    jobData = JobModel.objects.get(id=id)
    candidateData = CandidateProfileModel.objects.get(candidate_user= request.user)
    if request.method == 'POST':
        formData = JobApplyModelForm(request.POST)
        if formData.is_valid():
            jobApplyData = formData.save(commit=False)
            jobApplyData.job = jobData
            jobApplyData.candidate = candidateData
            jobApplyData.status = 'Applied'
            jobApplyData.save()
            return redirect('appliedJobList')
    else:
        formData = JobApplyModelForm()
    return render(request, 'apply_job.html',{'jobData':jobData,'formData':formData})