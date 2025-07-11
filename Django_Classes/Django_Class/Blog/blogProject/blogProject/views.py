from django.shortcuts import render

def homePage(request):
    return render(request, 'home.html')

def blogPage(request):
    return render(request, 'blog.html')

def userPage(request):
    return render(request, 'user.html')