from django.shortcuts import render ,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum



def signuppage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if CustomUserModel.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "signuppage.html")

        if password == confirm_password:
            user = CustomUserModel.objects.create_user(username=username, email=email, password=password)
            return redirect("login")
        else:
            messages.error(request, "Passwords do not match.")
            return render(request, "signuppage.html")
    return render(request, "signuppage.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "loginpage.html", {"error": "Invalid username or password."})
    return render(request, "loginpage.html")

def logout_view(request):
    logout(request)
    return redirect("login")


def homepage(request):
      today = timezone.now().date()
      month = today.month
      year = today.year

      total_income = AddcashModel.objects.filter(user=request.user).aggregate(total=Sum('amount'))['total'] or 0
      total_expense = ExpenceModel.objects.filter(user=request.user).aggregate(total=Sum('amount'))['total'] or 0

      monthly_income = AddcashModel.objects.filter(
        user=request.user,
        datetime__year=year,
        datetime__month=month
    ).aggregate(total=Sum('amount'))['total'] or 0

      monthly_expense = ExpenceModel.objects.filter(
        user=request.user,
        datetime__year=year,
        datetime__month=month
    ).aggregate(total=Sum('amount'))['total'] or 0
      daily_income = AddcashModel.objects.filter(user=request.user, datetime__date=today).aggregate(total=Sum('amount'))['total'] or 0
      daily_expense = ExpenceModel.objects.filter(user=request.user, datetime__date=today).aggregate(total=Sum('amount'))['total'] or 0
      balance = total_income - total_expense
      daily_balance=daily_income-daily_expense
      monthly_balance=monthly_income-monthly_expense

      total=DailyTotalModel.objects.filter(user=request.user,date=today).first()
      if total:
        total.total_cash_added = daily_income
        total.total_expenses = daily_expense
        total.net_balance = daily_balance
        total.save()
      else:
          DailyTotalModel.objects.create(
              user=request.user,
              date=today,
              total_cash_added=daily_income,
              total_expenses=daily_expense,
              net_balance=daily_balance,
          )
      daily_total=DailyTotalModel.objects.filter(user=request.user)

      context = {
          'total_income': total_income,
          'total_expense': total_expense,
          'daily_income': daily_income,
          'daily_expense': daily_expense,
          'balance': balance,
          'daily_balance': daily_balance,
          'monthly_expense' : monthly_expense,
          'monthly_income': monthly_income,
          'monthly_balance' : monthly_balance,
          'daily_total':daily_total

      }
      return render(request, "homepage.html",context)


def addcashpage(request):
    if request.method == "POST":
        form = AddcashForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("transaction")
    else:
        form = AddcashForm()
    return render(request, "addcash.html", {"form": form})

def addexpence(request):
    if request.method == "POST":
        form = ExpenceForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("transaction")
    else:
        form = ExpenceForm()
    return render(request, "addexpence.html", {"form": form})


def editcashpage(request,id):
    cash=AddcashModel.objects.get(id=id)
    if request.method == "POST":
        form = AddcashForm(request.POST, instance=cash)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("transaction")
    else:
        form = AddcashForm( instance=cash)
    return render(request, "addcash.html", {"form": form})

def editexpence(request,id):
    expence=ExpenceModel.objects.get(id=id)
    if request.method == "POST":
        form = ExpenceForm(request.POST, instance=expence)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("transaction")
    else:
        form = ExpenceForm(instance=expence)
    return render(request, "addexpence.html", {"form": form})
def deleteexpence(request,id):
   ExpenceModel.objects.get(id=id).delete()
   return redirect("transaction")

def deletecash(request,id):
   AddcashModel.objects.get(id=id).delete()
   return redirect("transaction")


def transaction(request):
    today = timezone.now().date()
    income = AddcashModel.objects.filter(user=request.user, datetime__date=today)
    expense = ExpenceModel.objects.filter(user=request.user, datetime__date=today)

    context={
          'expense_list':expense,
          'cash_list':income,
    }
    return render(request,'transaction.html',context)

def profile(request):
    return render(request, 'profile.html')


def editprofile(request):
    user = request.user
    if request.method == "POST":
        form = CustomUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = CustomUserForm(instance=user)
    return render(request, "editdprofile.html", {"form": form})


def changepass(request):
    if request.method == "POST":
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        user = authenticate(request, username=request.user.username, password=current_password)
        if user is not None:
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                return redirect("profile")
            else:
                messages.error(request, "New passwords do not match.")
        else:
            messages.error(request, "Current password is incorrect.")
    return render(request, "changepass.html")

