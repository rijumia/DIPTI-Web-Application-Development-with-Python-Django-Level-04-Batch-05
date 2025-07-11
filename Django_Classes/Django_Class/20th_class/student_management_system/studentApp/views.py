from django.shortcuts import render,redirect
from studentApp.models import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# <--------Home page Function-------------->
@login_required
def home(request):
    studentData = studentModel.objects.all()
    return render(request, 'home.html', {'student': studentData})

# <----------addStudent page Function-------------->
@login_required
def addStudent(request):
    if request.method == 'POST':
        profile_image = request.FILES.get('profile_image')
        name = request.POST.get('name')
        roll_number = request.POST.get('roll_number')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        is_active = request.POST.get('is_active') == 'on'

        studentData = studentModel(
            profile_image = profile_image,
            name = name,
            roll_number = roll_number,
            phone = phone,
            email = email,
            address = address,
            dob = dob,
            is_active = is_active,
        )
        studentData.save()
        return redirect('home')
    return render(request, 'addStudent.html')

# <----------editStudent page Function-------------->
@login_required
def editStudent(request,id):
    studentData = studentModel.objects.get(id=id)
    if request.method == 'POST':
        studentData.name = request.POST.get('name')
        studentData.roll_number = request.POST.get('roll_number')
        studentData.email = request.POST.get('email')
        studentData.phone = request.POST.get('phone')
        studentData.address = request.POST.get('address')
        studentData.dob = request.POST.get('dob')
        studentData.is_active = request.POST.get('is_active') == 'on'

        picture =request.FILES.get('profile_image')
        if picture is not None:
            studentData.profile_image = picture
        studentData.save()
        return redirect('home')
    return render(request, 'editStudent.html', {'student': studentData})

# <----------viewStudent page Function-------------->
@login_required
def viewStudent(request,id):
    studentData = studentModel.objects.get(id=id)
    return render(request, 'viewStudent.html', {'student': studentData})

# <----------deleteStudent page Function-------------->
@login_required
def deleteStudent(request,id):
    student = studentModel.objects.get(id=id)
    student.delete()
    return redirect('home')




# <----------loginPage Function-------------->
def loginPage(request):
    if request.method == 'POST':
        UserName = request.POST.get('userName')
        Password = request.POST.get('password')

        user = authenticate(username=UserName, password=Password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return redirect('passwordWrong')
    return render(request, 'loginPage.html')

# <----------logoutPage Function-------------->
def logoutPage(request):
    logout(request)
    return redirect('loginPage')

# <----------signupPage Function-------------->
def signupPage(request):
    if request.method == 'POST':
        userName = request.POST.get('userName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        if password == confirm_password:
            user = User.objects.create_user(userName, email, password)
            user.save()
            return redirect('loginPage')
        else:
            return redirect('passwordNotMatched')
    return render(request, 'signupPage.html')

# <----------passwordNotMatched Function-------------->
def passwordNotMatched(request):
    return render(request, 'passwordNotMatched.html')

# <----------passwordWrong Function-------------->
def passwordWrong(request):
    return render(request, 'passwordWrong.html')