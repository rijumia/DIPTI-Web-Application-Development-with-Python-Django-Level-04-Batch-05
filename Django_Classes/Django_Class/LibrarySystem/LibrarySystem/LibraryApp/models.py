from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    user_types = models.CharField(choices=[
        ('Librarian','Librarian'),
        ('Student','Student'),
    ],max_length=10, null=True)
    
class LibrarianProfileModel(models.Model):
    user = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE, related_name='librarian_profile',null=True)
    employee_id = models.IntegerField(null=True)
    designation = models.CharField(max_length=200, null=True)
    contact_number = models.CharField(max_length=15, null=True)
    address = models.TextField(null=True)
    profile_picture = models.ImageField(upload_to='media/profile')
    
class BookModel(models.Model):
    employee = models.ForeignKey(LibrarianProfileModel, on_delete=models.CASCADE, related_name='book', null=True)
    title = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=100, null=True)
    isbn = models.PositiveIntegerField(null=True)
    quantity = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class StudentProfileModel(models.Model):
    student_user = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE, related_name='student_profile',null=True)
    student_id =  models.IntegerField(null=True)
    department = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.TextField(null=True)
    profile_picture = models.ImageField(upload_to='media/profile')