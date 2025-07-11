from django.shortcuts import render
from storeApp.models import*

def homePage(request):
    return render(request, 'home.html')

def booksPage(request):
    bookData = bookModel.objects.all()
    context= {
        'data' : bookData
    }
    return render(request, 'books.html', context)

def userPage(request):
    userData = userModel.objects.all()
    context= {
        'data' : userData
    }
    return render(request, 'user.html', context)

