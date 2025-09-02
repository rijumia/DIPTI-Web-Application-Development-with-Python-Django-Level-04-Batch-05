from django.db import models

# Create your models here.
class CompanyModel(models.Model):
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class EmployeeModel(models.Model):
    DEPARTMENT_CHOICES = [
        ('HR', 'HR'),
        ('Manager', 'Manager'),
        ('Staff', 'Staff'),
    ]
    employee_name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return self.employee_name

class ProductModel(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

class JobModel(models.Model):
    title = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()

    def __str__(self):
        return self.title
