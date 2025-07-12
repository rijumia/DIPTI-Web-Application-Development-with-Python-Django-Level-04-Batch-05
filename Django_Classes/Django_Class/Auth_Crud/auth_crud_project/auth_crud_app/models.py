from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    role = [
        ('customer', 'Customer'),
        ('owner', 'Owner')
    ]
    user_type = models.CharField(choices=role, max_length=50, null=True)
    fullName = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    dateOfBirth = models.DateField(null=True)
    profileImage = models.ImageField(upload_to='Midea/profile')

class ProductModel(models.Model):
    productName = models.CharField(max_length=100)   
    productDescription = models.TextField(max_length=200)
    productPrice = models.PositiveIntegerField()
    productImage = models.ImageField(upload_to='Midea/product')