from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    user_types = models.CharField(choices=[
        ('Admin','Admin'),
        ('Employee','Employee'),
    ],max_length=10, null=True)
    
    def __str__(self):
        return self.username
    
class DepartmentModel(models.Model):
    Name = models.CharField(max_length=100, null=True)
    Description = models.TextField(null=True)
    
class EmployeeManagementModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, null=True)
    Department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE, null=True)
    FullName = models.CharField(max_length=200, null=True)
    Email = models.EmailField(null=True )
    Phone = models.CharField(max_length=15, null=True)
    Position = models.CharField(choices=[
        ('Administrative','Administrative'),
        ('StaffSupervision','StaffSupervision'),
        ('ResourceManagement','ResourceManagement'),
        ('Support','Support'),
        ('Staff','Staff'),
    ],max_length=50, null=True)
    Date_ofJoining = models.DateField(null=True)
    ProfilePicture = models.ImageField(upload_to='Media/ProfilePicture',null=True)
    
    def __str__(self):
        return self.FullName
    
class LeaveModel(models.Model):
    Employee = models.ForeignKey(EmployeeManagementModel, on_delete=models.CASCADE, null=True)
    LeaveType = models.CharField(choices=[
        ('casual_leave','casual_leave'),
        ('sick_leave','sick_leave'),
        ('earned_leave','earned_leave'),
        ('annual_leave','annual_leave'),
        ('maternity_leave','maternity_leave'),
    ],max_length=100,null=True)
    FromDate = models.DateField(null=True)
    ToDate = models.DateField(null=True)
    Reason = models.CharField(max_length=100, null=True)
    Status = models.CharField(choices=[
        ('Pending','Pending'),
        ('Approved','Approved'),
        ('Rejected','Rejected'),
    ],max_length=20,null=True)
    
    def __str__(self):
        return self.Status
    
