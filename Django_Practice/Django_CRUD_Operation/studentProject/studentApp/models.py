from django.db import models

class studentModel(models.Model):
    Student_Name = models.CharField(max_length=100)
    Student_Roll_No = models.CharField(max_length=20, unique=True)
    Student_Email = models.EmailField(max_length=100, unique=True)
    Student_Course = models.CharField(max_length=100)

class teacherModel(models.Model):
    Teacher_Name = models.CharField(max_length=100)
    Teacher_Email = models.EmailField(max_length=100, unique=True)
    Teacher_Department = models.CharField(max_length=100)
    Teacher_Experience = models.IntegerField()
