from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from JobApp.models import CustomUserModel, JobModel
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)

            return redirect('homePage')
    return render(request, 'login.html')

def signupPage(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        phone = request.POST.get('phone')
        bio = request.POST.get('bio')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = CustomUserModel.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                user_type = user_type,
                phone_no = phone,
                Bio = bio,
                password = password,
            )
            user.save()
            return redirect('loginPage')
    return render(request, 'signup.html')

@login_required
def changePasswordPage(request):
    current_user = request.user

    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        if check_password(old_password, current_user.password):
            if new_password1 == new_password2:
                current_user.set_password(new_password1)
                current_user.save()
                update_session_auth_hash(request, current_user)
                return redirect('homePage')

    return render(request, 'changePassword.html')

@login_required
def logoutPage(request):
    logout(request)
    return redirect('loginPage')

@login_required
def profilePage(request):
    return render(request, 'profile.html')

@login_required
def homePage(request):
    return render(request, 'home.html')

@login_required
def jobFeedPage(request):
    jobs = JobModel.objects.all()
    return render(request, 'jobFeed.html',{'jobs':jobs})

@login_required
def addJobPage(request):
    if request.method == 'POST':
        JobTitle = request.POST.get('JobTitle')
        JobDescription = request.POST.get('JobDescription')
        Job_type = request.POST.get('Job_type')
        CompanyLogo = request.FILES.get('CompanyLogo')

        JobModel.objects.create(
            CreateBy = request.user,
            JobTitle = JobTitle,
            JobDescription = JobDescription,
            Job_type = Job_type,
            CompanyLogo = CompanyLogo,
        )
        return redirect('jobFeedPage')
    return render(request, 'addJob.html')

@login_required
def jobViewPage(request,id):
    job = JobModel.objects.get(id=id)
    return render(request, 'jobView.html', {'job':job})

@login_required
def jobEditPage(request,id):
    jobUpdate = JobModel.objects.get(id=id)
    if request.method == 'POST':
        jobUpdate.JobTitle = request.POST.get('JobTitle')
        jobUpdate.JobDescription = request.POST.get('JobDescription')
        jobUpdate.Job_type = request.POST.get('Job_type')
       
        if request.FILES.get('CompanyLogo'):
             jobUpdate.CompanyLogo = request.FILES.get('CompanyLogo')

        jobUpdate.save()
        return redirect('jobFeedPage')
    return render(request, 'jobEdit.html',{'jobUpdate':jobUpdate})

@login_required
def jobDeletePage(request,id):
    job = JobModel.objects.get(id=id)
    job.delete()
    return redirect('jobFeedPage')