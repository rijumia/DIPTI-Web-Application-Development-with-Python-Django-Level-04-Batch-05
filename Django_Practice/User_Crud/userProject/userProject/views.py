from django.shortcuts import render, redirect
from userApp.models import userModel
import random

def homePage(request):

    user = userModel.objects.all()



    return render(request, 'home.html', {'users': user})

def addPage(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        full_name = f"{first_name} {last_name}"
        user_name = f"{first_name.lower()}_{last_name.lower()}_{random.randint(1000, 9999)}"

        # Create a new userModel instance
        new_user = userModel(
            First_Name=first_name,
            Last_Name=last_name,
            Full_Name=full_name,
            User_Name=user_name
        )
        new_user.save()
        return redirect('listPage')
    return render(request, 'addUser.html')

def listPage(request):
    users = userModel.objects.all()

    return render(request, 'userList.html', {'users': users})

def editPage(request, id):
    user = userModel.objects.get(id=id)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        full_name = f"{first_name} {last_name}"
        user_name = f"{first_name.lower()}_{last_name.lower()}_{random.randint(1000, 9999)}"

        # Update user
        user.First_Name = first_name
        user.Last_Name = last_name
        user.Full_Name = full_name
        user.User_Name = user_name
        user.save()

        return redirect('listPage')

    # Render the form with current user data
    return render(request, 'userUpdate.html', {'user': user})


def viewPage(request, id):
    users = userModel.objects.get(id=id)

    return render(request, 'userDetails.html', {'users': users})

def deletePage(request, id):
    users = userModel.objects.get(id=id)
    users.delete()
    return redirect('listPage')

