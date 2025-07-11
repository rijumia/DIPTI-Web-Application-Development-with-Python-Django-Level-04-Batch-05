from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from to_do_App.models import CustomUserModel, ToDoModel
from django.contrib.auth.hashers import check_password


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            return redirect('custom_error')
        
    return render(request, 'login.html')

def registerPage(request):
    if request.method == 'POST':
        user_image = request.FILES.get('user_image')
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        phone_number = request.POST.get('phone_number')
        city_name = request.POST.get('city_name')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            
            user = CustomUserModel.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_image=user_image,
                full_name=full_name,
                bio=bio,
                phone_number=phone_number,
                city_name=city_name,
                address=address
            )
            return redirect('loginPage')
        else:
            return redirect('custom_error')

    return render(request, 'register.html')

@login_required
def logoutPage(request):
    logout(request)
    return redirect('loginPage')

@login_required
def changePassword(request):
    current_user = request.user
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if current_user.check_password(old_password, current_user.password):
            if new_password == confirm_password:
                current_user.set_password(new_password)
                current_user.save()
                update_session_auth_hash(request, current_user)
                return redirect('loginPage')
        else:
            return redirect('custom_error')
        
    return render(request, 'changePassword.html')

@login_required
def homePage(request):
    total_task = ToDoModel.objects.filter(user=request.user)
    pending_task = ToDoModel.objects.filter(user=request.user, status='pending')
    in_progress_task = ToDoModel.objects.filter(user=request.user, status='in_progress')
    completed_task = ToDoModel.objects.filter(user=request.user, status='completed')

    return render(request, 'home.html', {
        'total_task': total_task,
        'pending_task': pending_task,
        'in_progress_task': in_progress_task,
        'completed_task': completed_task
    })

@login_required
def addToDo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')

        new_todo = ToDoModel.objects.create(
            user=request.user,
            title=title,
            description=description,
            status=status,
            due_date=due_date
        )
        return redirect('homePage')

    return render(request, 'add_todo.html')

@login_required
def listToDo(request):
    todos = ToDoModel.objects.filter(user=request.user)
    return render(request, 'list_todo.html', {'todos': todos})

@login_required
def viewToDo(request, id):
    todo = ToDoModel.objects.get(id=id, user=request.user)
    return render(request, 'view_todo.html', {'todo': todo})

@login_required
def editToDo(request, id):
    todo = ToDoModel.objects.get(id=id, user=request.user)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.status = request.POST.get('status')
        todo.due_date = request.POST.get('due_date')
        todo.save()
        return redirect('viewToDo', id=todo.id)
    return render(request, 'update_todo.html', {'todo': todo})

@login_required
def deleteToDo(request, id):
    todo = ToDoModel.objects.get(id=id, user=request.user)
    todo.delete()
    return redirect('listToDo')

def custom_error(request, exception=None):
    return render(request, 'Error.html', {'message': 'The requested page could not be found.'}, status=404)
