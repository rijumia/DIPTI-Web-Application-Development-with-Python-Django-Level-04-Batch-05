from django.db import models

# Create your models here.
class userModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    birth_date = models.DateField()

class studentModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    birth_date = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

class courseModel(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10)
    description = models.TextField()
    credits = models.IntegerField()
