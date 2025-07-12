from django.db import models

class ResumeModel(models.Model):
    Full_Name = models.CharField(max_length=100)
    Profile_Picture = models.ImageField(upload_to='Profile/picture')
    Email = models.EmailField()
    Phone = models.IntegerField()
    Address = models.TextField(max_length=50)
    Summary = models.TextField(max_length=100)
    Degree = models.CharField(max_length=50)
    Institute_Name = models.CharField(max_length=50)
    Year_of_Graduation = models.IntegerField()
    Company_Name = models.CharField(max_length=100)
    Position = models.CharField(max_length=20)
    Years_of_Experience = models.IntegerField()
    Skills = models.CharField(max_length=200)
    Hobbies = models.CharField(max_length=100)
    Achievements = models.CharField(max_length=200)
