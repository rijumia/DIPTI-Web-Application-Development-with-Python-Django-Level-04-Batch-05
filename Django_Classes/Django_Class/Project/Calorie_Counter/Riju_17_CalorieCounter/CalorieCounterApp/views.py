from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .models import *
from .forms import *
from django.contrib import messages
from datetime import date

# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if not username or not email or not password or not confirmPassword:
            messages.error(request, "All fields are required.")
            return redirect('registerPage')

        if CustomUserAuthModel.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('registerPage')

        if CustomUserAuthModel.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('registerPage')

        if password != confirmPassword:
            messages.error(request, "Passwords do not match.")
            return redirect('registerPage')

        user = CustomUserAuthModel.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        if user:
            UserProfileModel.objects.create(user=user)
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('loginPage')

    return render(request, 'register.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Both username and password are required.")
            return redirect('loginPage')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('loginPage')

    return render(request, 'login.html')



def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def profile(request):
    
    return render(request, 'profile.html')

def profileUpdate(request):
    current_user = request.user
    user_data = UserProfileModel.objects.get(user = current_user)
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=user_data)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = UserProfileForm(instance=user_data)
    return render(request, 'updateProfile.html',{'profile_form':profile_form})

def dashboard(request):
    daily_consumed = DailyConsumedModel.objects.all()
    total_consumed = TotalConsumedModel.objects.all()

    current_user = request.user
    gender = current_user.user_profile.gender
    height = current_user.user_profile.height
    weight = current_user.user_profile.weight
    age = current_user.user_profile.age
    today = date.today()
    today_consumed_calorie = TotalConsumedModel.objects.filter(user=request.user, date=today).first()
    
    w = weight or 0
    h = height or 0
    a = age or 0

    if gender == 'Male':
        BMR = 66.47 + (13.75 * w) + (5.003 * h) - (6.755 * a)
    else:
        BMR = 655.1 + (9.563 * w) + (1.850 * h) - (4.676 * a)
    BMR = round(BMR,2)

    today_consumed_calorie = today_consumed_calorie.totalCalorie if today_consumed_calorie else 0
    remaining_calorie = round(BMR - today_consumed_calorie, 2)
    context={
        'daily_consumed':daily_consumed,
        'total_consumed':total_consumed,
        'BMR':BMR,
        'today_consumed_calorie':today_consumed_calorie,
        'remaining_calorie':remaining_calorie
    }
    return render(request, 'dashboard.html',context)

def addCalorie(request):
    if request.method == 'POST':
        calorie_form = DailyConsumedForm(request.POST)
        if calorie_form.is_valid():
            entry = calorie_form.save(commit=False)
            entry.user = request.user
            entry.save()
            date = entry.date

            total_entry, created = TotalConsumedModel.objects.get_or_create(
                user=request.user,
                date=date,
                defaults={'totalCalorie': entry.calories}
            )
            if not created:
                total_entry.totalCalorie += entry.calories
                total_entry.save()

            return redirect('dashboard')
    else:
        calorie_form = DailyConsumedForm() 
    return render(request, 'addCalorie.html', {'calorie_form': calorie_form})

def update_calorie(request, pk):
    calorie_data = DailyConsumedModel.objects.get(id=pk, user=request.user)

    old_calories = calorie_data.calories
    old_date = calorie_data.date

    if request.method == 'POST':
        calorie_form = DailyConsumedForm(request.POST, instance=calorie_data)
        if calorie_form.is_valid():
            entry = calorie_form.save(commit=False)
            entry.user = request.user
            entry.save()

            old_total = TotalConsumedModel.objects.filter(user=request.user, date=old_date).first()
            if old_total:
                old_total.totalCalorie -= old_calories
                if old_total.totalCalorie <= 0:
                    old_total.delete()
                else:
                    old_total.save()

            new_total, created = TotalConsumedModel.objects.get_or_create(
                user=request.user,
                date=entry.date,
                defaults={'totalCalorie': entry.calories}
            )
            if not created:
                new_total.totalCalorie += entry.calories
                new_total.save()

            return redirect('dashboard')
    else:
        calorie_form = DailyConsumedForm(instance=calorie_data)

    return render(request, 'update_calorie.html', {'calorie_form': calorie_form})

def delete_calorie(request, pk):
    calorie_entry = DailyConsumedModel.objects.get(id=pk, user=request.user)

    total_entry = TotalConsumedModel.objects.filter(user=request.user, date=calorie_entry.date).first()
    if total_entry:
        total_entry.totalCalorie -= calorie_entry.calories
        if total_entry.totalCalorie <= 0:
            total_entry.delete()
        else:
            total_entry.save()

    calorie_entry.delete()

    return redirect('dashboard')