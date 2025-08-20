from django.db import models

# Create your models here.
class CompanyModel(models.Model):
    companyName = models.CharField(max_length=150, null=True)
    location = models.CharField(max_length=200, null=True)
    contact = models.CharField(max_length=15, null=True)

class EmployeeModel(models.Model):
    employeeName = models.CharField(max_length=150, null=True)
    price = models.PositiveIntegerField(null=True)
    quantity = models.PositiveIntegerField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)

class ProductModel(models.Model):
    productName = models.CharField(max_length=150, null=True)
    price = models.PositiveIntegerField(null=True)
    quantity = models.PositiveIntegerField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)

class JobModel(models.Model):
    title = models.CharField(max_length=150, null=True)
    designation = models.CharField(max_length=150, null=True)
    salary = models.PositiveIntegerField(null=True)
    deadline = models.DateField(null=True)
    
