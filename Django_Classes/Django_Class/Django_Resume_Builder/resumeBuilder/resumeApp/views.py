from django.shortcuts import render, redirect
from resumeApp.models import ResumeModel

def home(req):
    resumes = ResumeModel.objects.all()
    return render(req, 'home.html', {'resumes': resumes})

def addDetails(req):
    if req.method == 'POST':
        fullName = req.POST.get('fullName')
        profilePicture = req.FILES.get('profilePicture')
        email = req.POST.get('email')
        phone = req.POST.get('phone')
        address = req.POST.get('address')
        summary = req.POST.get('summary')
        degree = req.POST.get('degree')
        institute = req.POST.get('institute')
        graduationYear = req.POST.get('graduationYear')
        company = req.POST.get('company')
        position = req.POST.get('position')
        experience = req.POST.get('experience')
        skills = req.POST.get('skills')
        hobbies = req.POST.get('hobbies')
        achievements = req.POST.get('achievements')

        resumeData = ResumeModel(
            Full_Name = fullName,
            Profile_Picture = profilePicture,
            Email = email,
            Phone = phone,
            Address = address,
            Summary = summary,
            Degree = degree,
            Institute_Name = institute,
            Year_of_Graduation = graduationYear,
            Company_Name = company,
            Position = position,
            Years_of_Experience = experience,
            Skills = skills,
            Hobbies = hobbies,
            Achievements = achievements,
        )
        resumeData.save()
        return redirect('home')
    return render(req, 'addDetails.html')

def updateDetails(req, id):
    resume = ResumeModel.objects.get(id=id)

    if req.method == 'POST':
        resume.Full_Name = req.POST.get('fullName')
        resume.Email = req.POST.get('email')
        resume.Phone = req.POST.get('phone')
        resume.Address = req.POST.get('address')
        resume.Summary = req.POST.get('summary')
        resume.Degree = req.POST.get('degree')
        resume.Institute_Name = req.POST.get('institute')
        resume.Year_of_Graduation = req.POST.get('graduationYear')
        resume.Company_Name = req.POST.get('company')
        resume.Position = req.POST.get('position')
        resume.Years_of_Experience = req.POST.get('experience')
        resume.Skills = req.POST.get('skills')
        resume.Hobbies = req.POST.get('hobbies')
        resume.Achievements = req.POST.get('achievements')
        if req.FILES.get('profilePicture'):
            resume.Profile_Picture=req.FILES.get('profilePicture')


        resume.save()
        return redirect('home')
    return render(req, 'updateDetails.html', {'resume': resume})

def detailsList(req):
    resumes = ResumeModel.objects.all()
    return render(req, 'detailsList.html', {'resumes': resumes})

def deleteResume(req, id):
    resume = ResumeModel.objects.get(id=id)
    resume.delete()
    return redirect('home')