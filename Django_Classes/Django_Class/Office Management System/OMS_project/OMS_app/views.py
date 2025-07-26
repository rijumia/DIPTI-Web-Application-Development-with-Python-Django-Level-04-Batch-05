from django.shortcuts import render,redirect
from django.contrib.auth import login,logout, authenticate, update_session_auth_hash
from OMS_app.models import *
from django.contrib import messages
from datetime import timedelta

# Create your views here.
def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            CustomUserModel.objects.create_user(
                username = username,
                email = email,
                user_types = user_type,
                password = confirm_password,
            )
            return redirect('loginPage')
    return render(request, 'signup.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboardPage')
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')


def dashboardPage(request):
    user = request.user

    if user.user_types == 'Admin':
        total_employees = EmployeeManagementModel.objects.count()
        total_departments = DepartmentModel.objects.count()
        pending_leaves = LeaveModel.objects.filter(Status='Pending').count()

        return render(request, 'dashboard.html', {
            'total_employees': total_employees,
            'total_departments': total_departments,
            'pending_leaves': pending_leaves
        })

    elif user.user_types == 'Employee':
        employee_profile = EmployeeManagementModel.objects.get(user=user)
        leaves = LeaveModel.objects.filter(Employee=employee_profile)

        leave_summary = {
            'total': leaves.count(),
            'approved': leaves.filter(Status='Approved').count(),
            'pending': leaves.filter(Status='Pending').count(),
            'rejected': leaves.filter(Status='Rejected').count(),
        }

        return render(request, 'dashboard.html', {
            'employee_profile': employee_profile,
            'leave_summary': leave_summary
        })

    return redirect('loginPage')

    

def addDepartmentPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        
        DepartmentModel.objects.create(
            Name = name,
            Description = description,
        )
        return redirect('departmentPage')
    return render(request, 'departments/addDepartment.html')

def departmentPage(request):
    departs = DepartmentModel.objects.all()
    return render(request, 'departments/departmentList.html',{'departs':departs})

def addEmployeePage(request):
    departments = DepartmentModel.objects.all()
    
    if request.method == 'POST':
        department_id = request.POST.get('department')
        profile_pic = request.FILES.get('profile_pic')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        position = request.POST.get('position')
        joining_date = request.POST.get('joining_date')
        
        user = CustomUserModel.objects.create_user(
            username = email,
            password= phone,
            user_types = 'Employee'
        )
        
        if user:
            employee = EmployeeManagementModel.objects.create(
                user = user,
                Department_id  = department_id,
                ProfilePicture = profile_pic,
                FullName = full_name,
                Email = email,
                Phone = phone,
                Position = position,
                Date_ofJoining = joining_date,
            
            )
            return redirect('employeePage')
    return render(request, 'add_employee.html',{'departments':departments})

def employeePage(request):
    employees = EmployeeManagementModel.objects.all()
    return render(request, 'employee.html',{'employees':employees})

def leaveRequestPage(request):
    leaveRequests = LeaveModel.objects.all()
    for leave in leaveRequests:
        duration = (leave.ToDate - leave.FromDate).days + 1
        leave.total_days = duration
    return render(request, 'leaveRequest.html',{'leaveRequests':leaveRequests})

def ApprovePage(request, id):
    leave = LeaveModel.objects.get(id=id)
    if leave.Status == 'Pending':
        leave.Status = 'Approved'
        leave.save()
        
    return redirect('leaveRequestPage')

def RejectedPage(request, id):
    leave = LeaveModel.objects.get(id=id)
    if leave.Status == 'Pending':
        leave.Status = 'Rejected'
        leave.save()
        
    return redirect('leaveRequestPage')

def addLeavePage(request):
    
    if request.method == 'POST':
        leave_type = request.POST.get('leave_type')
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        reason = request.POST.get('reason')
        
        try:
            current_employee = EmployeeManagementModel.objects.get(user=request.user)
        except EmployeeManagementModel.DoesNotExist:
            messages.error(request, "Employee profile not found.")
            return redirect('dashboardPage')  
        
        LeaveModel.objects.create(
            Employee = current_employee,
            LeaveType = leave_type,
            FromDate = from_date,
            ToDate = to_date,
            Reason = reason,
            Status = 'Pending',
        )
        return redirect('leaveListPage')
    return render(request, 'employee/addLeaveRequest.html')

def leaveListPage(request):
    employee = EmployeeManagementModel.objects.get(user=request.user)
    leave_requests = LeaveModel.objects.filter(Employee=employee)
    return render(request, 'employee/leaveStatus.html',{'leave_requests':leave_requests})

def profilePage(request):
    employee = EmployeeManagementModel.objects.get(user=request.user)
    return render(request, 'employee/profile.html',{'employee':employee})