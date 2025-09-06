from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserAuthModel(AbstractUser):

    def __str__(self):
        return self.username
    
class UserProfileModel(models.Model):
    user = models.OneToOneField(CustomUserAuthModel, on_delete=models.CASCADE, null=True, related_name='user_profile')
    name = models.CharField(max_length=200, null=True)
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(choices=[
        ('Male', "Male"),
        ('Female', 'Female'),
    ], max_length=10, null=True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)

    def __str__(self):
        return self.user.username
    


class DailyConsumedModel(models.Model):
    user = models.ForeignKey(CustomUserAuthModel, on_delete=models.CASCADE, related_name='user_daily_calorie')
    itemName = models.CharField(max_length=250, null=True)
    calories = models.FloatField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return f'{self.user.username}-{self.itemName}-{self.calories}'
    

class TotalConsumedModel(models.Model):
    user = models.ForeignKey(CustomUserAuthModel, on_delete=models.CASCADE, null=True, related_name='user_total_calorie')
    totalCalorie = models.FloatField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return f'{self.user.username}-{self.totalCalorie}-{self.date}'