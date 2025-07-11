from django.shortcuts import render,redirect,get_object_or_404
from customUsersApp.models import customUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def loginPage(request):
    if request.method == 'POST':
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        
        user = authenticate(username=Username, password=Password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def signupPage(request):
    if request.method == 'POST':
        Username = request.POST.get('Username')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        Confirm_Password = request.POST.get('Confirm_Password')
        role = request.POST.get('role')
        age = request.POST.get('age')
        mobile = request.POST.get('mobile')
        description = request.POST.get('description')
        instutiteName = request.POST.get('instutiteName')
        passingYear = request.POST.get('passingYear')
        workExperience = request.POST.get('workExperience')
        image = request.FILES.get('image')

        if Password == Confirm_Password:
            user = customUser.objects.create_user(
                username=Username,
                email=Email,
                password=Confirm_Password,
                user_type=role,
                age=age if age else None,
                mobile=mobile,
                description=description,
                instutiteName=instutiteName,
                passingYear=passingYear if passingYear else None,
                workExperience=workExperience if workExperience else None,
                image=image,
            )
            return redirect('loginPage')
        else:
            return render(request, 'signup.html', {'error': 'Passwords do not match!'})

    return render(request, 'signup.html')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')


def homePage(request):
    return render(request, 'home.html')

def listPage(request):
    users = customUser.objects.all()
    return render(request, 'list.html', {'users': users})

def deletePage(request, id):
    user = customUser.objects.get(id=id)
    user.delete()
    return redirect('listPage')

def view_detail(request, id):
    user = get_object_or_404(customUser, pk=id)
    return render(request, 'view_detail.html', {'user': user})

def updatePage(request, pk):
    user = get_object_or_404(customUser, pk=pk)

    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.age = request.POST.get('age')
        user.mobile = request.POST.get('mobile')
        user.description = request.POST.get('description')
        user.instutiteName = request.POST.get('instutiteName')
        user.passingYear = request.POST.get('passingYear')
        user.workExperience = request.POST.get('workExperience')

        if request.FILES.get('image'):
            user.image = request.FILES['image']

        user.save()
        return redirect('resume_detail', pk=user.pk)
    
    return render(request, 'update.html', {'user': user})
