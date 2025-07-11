from django.shortcuts import render, redirect
from userApp.models import userModel
import random

# def homePage(request):
#     user = userModel.objects.all()
#     context={
#         'user':user
#     }
#     return render(request, 'home.html', context)
def homePage(request):
    users = userModel.objects.all()
    return render(request, 'home.html', {'users': users})


def addUserPage(request):
    if request.method=='POST':
        User_First_Name= request.POST.get('firstname')
        User_Last_Name = request.POST.get('lastname')

        User_full_Name = User_First_Name +' '+ User_Last_Name
        User_extra = random.randint(100, 999)
        User_name = User_First_Name + str(User_extra)

        user_data = userModel(
            User_Name = User_name,
            User_First_Name = User_First_Name,
            User_Last_Name = User_Last_Name,
            User_Full_Name = User_full_Name
        )
        user_data.save()
        return redirect('/')

    return render(request, 'addUser.html')