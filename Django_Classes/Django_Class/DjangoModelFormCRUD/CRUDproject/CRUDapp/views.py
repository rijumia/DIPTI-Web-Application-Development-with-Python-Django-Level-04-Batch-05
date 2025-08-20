from django.shortcuts import render, redirect
from CRUDapp.models import *
from CRUDapp.forms import *

# Create your views here.
def homePage(request):
    return render(request, 'home.html')

def companyList(request):
    companies = CompanyModel.objects.all()
    return render(request, 'companyList.html',{'companies':companies})

def addCompany(request):
    if request.method == 'POST':
        form = CompanyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('companyList')
    else:
        form = CompanyModelForm()  
    return render(request, 'addCompany.html', {'form':form})

def updateCompany(request, id):
    company = CompanyModel.objects.get(id=id)

    if request.method == 'POST':
        form = CompanyModelForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('companyList')
    else:
        form = CompanyModelForm(instance=company)  

    return render(request, 'updateCompany.html', {'form': form})

def deleteCompany(request, id):
    company = CompanyModel.objects.get(id=id)
    company.delete()
    return redirect('companyList')


def addEmployee(request):
    if request.method == 'POST':
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employeeList')
    else:
        form = EmployeeModelForm()  
    return render(request, 'addEmployee.html', {'form':form})

def employeeList(request):
    employees = EmployeeModel.objects.all()
    return render(request, 'employeeList.html',{'employees':employees})

def updateEmployee(request, id):
    company = EmployeeModel.objects.get(id=id)

    if request.method == 'POST':
        form = EmployeeModelForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('employeeList')
    else:
        form = EmployeeModelForm(instance=company)  

    return render(request, 'updateCompany.html', {'form': form})

def deleteEmployee(request, id):
    company = EmployeeModel.objects.get(id=id)
    company.delete()
    return redirect('employeeList')


def addProduct(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productList')
    else:
        form = ProductModelForm()  
    return render(request, 'addProduct.html', {'form':form})

def productList(request):
    employees = ProductModel.objects.all()
    return render(request, 'productList.html',{'employees':employees})

def updateProduct(request, id):
    company = ProductModel.objects.get(id=id)

    if request.method == 'POST':
        form = ProductModelForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('productList')
    else:
        form = ProductModelForm(instance=company)  

    return render(request, 'updateProduct.html', {'form': form})

def deleteProduct(request, id):
    company = ProductModel.objects.get(id=id)
    company.delete()
    return redirect('productList')



def addJob(request):
    if request.method == 'POST':
        form = JobModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobList')
    else:
        form = JobModelForm()  
    return render(request, 'addJob.html', {'form':form})

def jobList(request):
    employees = JobModel.objects.all()
    return render(request, 'jobList.html',{'employees':employees})

def updateJob(request, id):
    company = JobModel.objects.get(id=id)

    if request.method == 'POST':
        form = JobModelForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('jobList')
    else:
        form = JobModelForm(instance=company)  

    return render(request, 'updateJob.html', {'form': form})

def deleteJob(request, id):
    company = JobModel.objects.get(id=id)
    company.delete()
    return redirect('jobList')