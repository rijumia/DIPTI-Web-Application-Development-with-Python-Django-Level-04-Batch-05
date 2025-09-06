from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUserModel(AbstractUser):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)


class AddcashModel(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='addcash')
    source = models.CharField(max_length=100, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    description = models.TextField(null=True, blank=True)


class ExpenceModel(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='addexpence')
    description = models.TextField(null=True, blank=True)
    amount = models.FloatField()
    datetime = models.DateTimeField(auto_now_add=True)


class DailyTotalModel(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='dailytotal')
    date = models.DateField()
    total_cash_added = models.FloatField()
    total_expenses = models.FloatField()
    net_balance = models.FloatField()
  
    