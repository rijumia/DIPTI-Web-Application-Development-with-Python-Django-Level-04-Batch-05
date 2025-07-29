from django.db import models

# Create your models here.
class StudentModel(models.Model):
    studentRoll = models.PositiveIntegerField(null=True)
    studentUsername = models.CharField(max_length=50, null=True)
    studentName = models.CharField(max_length=100, null=True)
    studentAddress = models.TextField(null=True)
    studentAge = models.IntegerField(null=True)
    studentRegisterdate = models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.studentName
    