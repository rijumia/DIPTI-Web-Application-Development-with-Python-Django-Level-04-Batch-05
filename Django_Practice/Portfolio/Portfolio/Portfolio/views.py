from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, ContactForm, ProfileForm
from .models import Profile, Skill, Project, Experience, Education

def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created. Please log in.")
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        data = request.POST.copy()
        identifier = data.get('username')
        try:
            user_obj = User.objects.get(email=identifier)
            data['username'] = user_obj.username
        except User.DoesNotExist:
            pass
        form = LoginForm(request, data=data)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        pform = ProfileForm(request.POST, request.FILES, instance=profile)
        if pform.is_valid():
            pform.save()
            messages.success(request, "Profile updated.")
            return redirect('dashboard')
    else:
        pform = ProfileForm(instance=profile)
    context = {
        'profile': profile,
        'pform': pform,
        'skills': Skill.objects.filter(profile=profile),
        'projects': Project.objects.filter(profile=profile),
        'experiences': Experience.objects.filter(profile=profile),
        'education': Education.objects.filter(profile=profile),
    }
    return render(request, 'dashboard.html', context)

def resume_view(request, username):
    user = get_object_or_404(User, username=username)
    profile, _ = Profile.objects.get_or_create(user=user)
    context = {
        'profile': profile,
        'skills': Skill.objects.filter(profile=profile),
        'projects': Project.objects.filter(profile=profile),
        'experiences': Experience.objects.filter(profile=profile),
        'education': Education.objects.filter(profile=profile),
    }
    return render(request, 'resume.html', context)

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for your message.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
