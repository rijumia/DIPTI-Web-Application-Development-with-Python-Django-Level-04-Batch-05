from django.shortcuts import render, redirect, HttpResponse
from instituteApp.models import CustomUserModel, TeacherModel, StudentModel

def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        usertype = request.POST.get('usertype')
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        if password == confirm_password:
            userData = CustomUserModel.objects.create_user(
                username = username,
                password= password,
                email = email,
                user_type = usertype,
            )
            userData.save()

            if userData:
                if userData.user_type == 'teacher':
                    TeacherModel.objects.create(
                        user = userData,
                        full_name = fullname,
                        address= address,
                        contact_number = contact,
                        designation = designation,
                    )
                else:
                    StudentModel.objects.create(
                        user = userData,
                        full_name = fullname,
                        address= address,
                        contact_number = contact,
                        department = department,
                    )
                    return redirect('loginPage')
        else:
            return HttpResponse('Passwords do not match.')

    return render(request, 'register.html')
