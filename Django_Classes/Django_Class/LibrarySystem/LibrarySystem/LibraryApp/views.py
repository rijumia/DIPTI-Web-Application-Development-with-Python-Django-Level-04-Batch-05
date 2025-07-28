from django.shortcuts import render, redirect
from LibraryApp.models import *
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.hashers import check_password
from LibraryApp.forms import *


# Create your views here.
def signupPage(request):
    if request.method == 'POST':
        Profile = request.FILES.get('Profile')
        id = request.POST.get('id')
        username = request.POST.get('username')
        Designation = request.POST.get('Designation')
        Department = request.POST.get('Department')
        phone = request.POST.get('phone')
        Address = request.POST.get('Address')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if password == confirmPassword:
            user = CustomUserModel.objects.create_user(
                username= username,
                user_types = user_type,
                password=password,
            )
            
            if user:
                if user.user_types == 'Librarian':
                    LibrarianProfileModel.objects.create(
                        user = user,
                        employee_id = id,
                        designation = Designation,
                        contact_number = phone,
                        address = Address,
                        profile_picture = Profile,
                    )
                elif user.user_types == 'Student':
                    StudentProfileModel.objects.create(
                        student_user = user,
                        student_id = id,
                        department = Department,
                        phone = phone,
                        address = Address,
                        profile_picture = Profile,
                    )
                    
            return redirect('loginPage')
    return render(request, 'signup.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboardPage')
    return render(request, 'login.html')

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
                return redirect('dashboardPage')
    return render(request, 'changePassword.html')

def logOutPage(request):
    logout(request)
    return redirect('loginPage')

def profilePage(request):
    if request.user.user_types == 'Librarian':
        profile_info = LibrarianProfileModel.objects.get(user=request.user)
    elif request.user.user_types == 'Student':
        profile_info= StudentProfileModel.objects.get(student_user = request.user)
    return render(request, 'profile.html',{'profile_info':profile_info})

def updateProfilePage(request):
    user = request.user

    if user.user_types == 'Librarian':
        profile = LibrarianProfileModel.objects.get(user=user)
        form_class = LibrarianProfileForm
    elif user.user_types == 'Student':
        profile = StudentProfileModel.objects.get(student_user=user)
        form_class = StudentProfileForm

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profilePage')
    else:
        form = form_class(instance=profile)

    return render(request, 'updateProfile.html', {'form': form})

def dashboardPage(request):
    books = BookModel.objects.all()
    return render(request, 'dashboard.html',{'books':books})

def bookListPage(request):
    if request.user.user_types == 'Librarian':
        librarian_profile = LibrarianProfileModel.objects.get(user=request.user)
        books = BookModel.objects.filter(employee=librarian_profile)
    elif request.user.user_types == 'Student':
        books = BookModel.objects.all()
    return render(request, 'book/book_list.html',{'books':books})

def addBookPage(request):
    if request.method == 'POST':
        form_info = BookModelForm(request.POST)
        if form_info.is_valid():
            book = form_info.save(commit=False)
            book.employee = request.user.librarian_profile
            book.save()
            return redirect('bookListPage')
    else:
        form_info = BookModelForm()
    return render(request, 'book/addBook.html', {'form_info': form_info})


def updateBookPage(request, book_id):
    book = BookModel.objects.get(id=book_id)
    if book.employee.user != request.user:
        return redirect('bookListPage')
    if request.method == 'POST':
        form = BookModelForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('bookListPage')
    else:
        form = BookModelForm(instance=book)

    return render(request, 'book/updateBook.html', {'form_info': form})


def deleteBookPage(request, book_id):
    book = BookModel.objects.get(id=book_id)
    if book.employee.user == request.user:
        book.delete()
    return redirect('bookListPage')



