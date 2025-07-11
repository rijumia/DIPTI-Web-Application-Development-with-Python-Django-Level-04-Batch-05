from django.shortcuts import render,redirect,HttpResponse
from book.models import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirm_password')

        if password == confirmPassword:
            user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('loginPage')
    return render(request, 'registerPage.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
        else:
            return HttpResponse('username or password not matched')
        user.save()

        return redirect('home')

    return render(request, 'loginPage.html')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')


def home(request):
    bookData = bookModel.objects.all()
    return render(request, 'home.html', {'book': bookData})
def addBook(request):
    if request.method == 'POST':
        bookImage = request.FILES.get('bookImage')
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')

        book = bookModel(
            bookImage = bookImage,
            title = title,
            author = author,
            description = description,
        )
        book.save()
        return redirect('home')
    return render(request, 'addBook.html')
def editBook(request,id):
    bookData = bookModel.objects.get(id=id)
    if request.method == 'POST':
        bookData.title = request.POST.get('title')
        bookData.author = request.POST.get('author')
        bookData.description = request.POST.get('description')

        picture =request.FILES.get('bookImage')
        if picture is not None:
            bookData.bookImage = picture
        bookData.save()
        return redirect('home')
    return render(request, 'editBook.html', {'book': bookData})
def viewBook(request,id):
    bookData = bookModel.objects.get(id=id)
    return render(request, 'viewBook.html', {'book': bookData})
def deleteBook(request,id):
    bookModel.objects.get(id=id).delete()
    return redirect('home')