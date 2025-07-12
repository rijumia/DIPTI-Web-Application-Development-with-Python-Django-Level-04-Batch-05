from django.db import models

class studentModel(models.Model):
    StudentName = models.CharField(max_length=100)
    StudentAddress = models.TextField(max_length=200)
    StudentDepartment = models.CharField(max_length=100)
    StudentAge = models.IntegerField()
