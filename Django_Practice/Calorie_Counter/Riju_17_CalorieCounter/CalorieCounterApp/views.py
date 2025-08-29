from django.shortcuts import render, redirect

# Create your views here.
def registerPage(request):
    return render(request, 'register.html')

def loginPage(request):
    return render(request, 'login.html')