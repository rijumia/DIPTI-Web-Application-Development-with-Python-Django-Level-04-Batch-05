from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View

from .forms import (CustomUserCreationForm, CustomAuthenticationForm, ContactForm, 
                    SkillForm, ProjectForm, WorkExperienceForm, EducationForm)

from .models import (CustomUser, Skill, Project, WorkExperience, Education, ContactMessage)

# Registration view
def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login view
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username/email or password.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have logged out successfully.")
    return redirect('login')

# Dashboard view (CRUD overview)
@login_required
def dashboard_view(request):
    user = request.user
    skills = user.skills.all()
    projects = user.projects.all()
    work_experiences = user.work_experiences.all()
    educations = user.educations.all()
    return render(request, 'dashboard.html', {
        'skills': skills,
        'projects': projects,
        'work_experiences': work_experiences,
        'educations': educations,
    })

# All CRUD operations for each model:
# Using function-based views for add/edit/delete

# Skill CRUD
@login_required
def skill_add(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            messages.success(request, "Skill added.")
            return redirect('dashboard')
    else:
        form = SkillForm()
    return render(request, 'skill_form.html', {'form': form, 'title': 'Add Skill'})

@login_required
def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk, user=request.user)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill updated.")
            return redirect('dashboard')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'skill_form.html', {'form': form, 'title': 'Edit Skill'})

@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk, user=request.user)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, "Skill deleted.")
        return redirect('dashboard')
    return render(request, 'skill_confirm_delete.html', {'object': skill})

# Project CRUD
@login_required
def project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            messages.success(request, "Project added.")
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form, 'title': 'Add Project'})

@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project updated.")
            return redirect('dashboard')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_form.html', {'form': form, 'title': 'Edit Project'})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project deleted.")
        return redirect('dashboard')
    return render(request, 'project_confirm_delete.html', {'object': project})

# WorkExperience CRUD
@login_required
def work_add(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.user = request.user
            work.save()
            messages.success(request, "Work experience added.")
            return redirect('dashboard')
    else:
        form = WorkExperienceForm()
    return render(request, 'work_form.html', {'form': form, 'title': 'Add Work Experience'})

@login_required
def work_edit(request, pk):
    work = get_object_or_404(WorkExperience, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST, instance=work)
        if form.is_valid():
            form.save()
            messages.success(request, "Work experience updated.")
            return redirect('dashboard')
    else:
        form = WorkExperienceForm(instance=work)
    return render(request, 'work_form.html', {'form': form, 'title': 'Edit Work Experience'})

@login_required
def work_delete(request, pk):
    work = get_object_or_404(WorkExperience, pk=pk, user=request.user)
    if request.method == 'POST':
        work.delete()
        messages.success(request, "Work experience deleted.")
        return redirect('dashboard')
    return render(request, 'work_confirm_delete.html', {'object': work})

# Education CRUD
@login_required
def education_add(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            educ = form.save(commit=False)
            educ.user = request.user
            educ.save()
            messages.success(request, "Education added.")
            return redirect('dashboard')
    else:
        form = EducationForm()
    return render(request, 'education_form.html', {'form': form, 'title': 'Add Education'})

@login_required
def education_edit(request, pk):
    educ = get_object_or_404(Education, pk=pk, user=request.user)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=educ)
        if form.is_valid():
            form.save()
            messages.success(request, "Education updated.")
            return redirect('dashboard')
    else:
        form = EducationForm(instance=educ)
    return render(request, 'education_form.html', {'form': form, 'title': 'Edit Education'})

@login_required
def education_delete(request, pk):
    educ = get_object_or_404(Education, pk=pk, user=request.user)
    if request.method == 'POST':
        educ.delete()
        messages.success(request, "Education deleted.")
        return redirect('dashboard')
    return render(request, 'education_confirm_delete.html', {'object': educ})

# Public portfolio display
def portfolio_view(request, username=None):
    # If username specified, show portfolio of that user, else default to admin user
    if username:
        user = get_object_or_404(CustomUser, username=username)
    else:
        user = CustomUser.objects.filter(is_superuser=True).first()
    if not user:
        return render(request, 'portfolio_not_found.html', status=404)
    skills = user.skills.all()
    projects = user.projects.all()
    work_experiences = user.work_experiences.all()
    educations = user.educations.all()

    return render(request, 'portfolio.html', {
        'portfolio_user': user,
        'skills': skills,
        'projects': projects,
        'work_experiences': work_experiences,
        'educations': educations,
    })

# CV / Resume view (show all data in printable form)
def resume_view(request, username=None):
    if username:
        user = get_object_or_404(CustomUser, username=username)
    else:
        user = CustomUser.objects.filter(is_superuser=True).first()

    skills = user.skills.all()
    projects = user.projects.all()
    work_experiences = user.work_experiences.all()
    educations = user.educations.all()

    return render(request, 'resume.html', {
        'portfolio_user': user,
        'skills': skills,
        'projects': projects,
        'work_experiences': work_experiences,
        'educations': educations,
    })

# Contact form view
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message was sent successfully.")
            return redirect('contact')
        else:
            messages.error(request, "Please correct errors below.")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})