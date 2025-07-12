from django.shortcuts import render,redirect,HttpResponse
from newsApp.models import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# --------------Authentication-------------------->
def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
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
            return HttpResponse('user name or password not matched')
        return redirect('home')
    return render(request, 'loginPage.html')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')

# ---------------CRUD--------------------------->
def home(request):
    newsData = newsModel.objects.all()
    return render(request, 'home.html', {'news': newsData})
def addNews(request):
    if request.method == 'POST':
        thumbnail = request.FILES.get('thumbnail')
        title = request.POST.get('title')
        content = request.POST.get('content')
        published_date = request.POST.get('published_date')

        news = newsModel(
            thumbnail = thumbnail,
            title = title,
            content = content,
            published_date =published_date,
        )
        news.save()
        return redirect('home')
    return render(request, 'addNews.html')
def editNews(request, id):
    newsData = newsModel.objects.get(id=id)
    if request.method == 'POST':
        newsData.title = request.POST.get('title')
        newsData.content = request.POST.get('content')

        picture = request.FILES.get('thumbnail')
        if picture is not None:
            newsData.thumbnail = picture
        newsData.save()
        return redirect('home')
    return render(request, 'editNews.html', {'news': newsData})
def viewNews(request, id):
    newsData = newsModel.objects.get(id=id)
    return render(request, 'viewNews.html', {'news': newsData})
def deleteNews(request, id):
    newsModel.objects.get(id=id).delete()
    return redirect('home')