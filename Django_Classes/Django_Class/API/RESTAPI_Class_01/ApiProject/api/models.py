from django.db import models

# Create your models here.
class StudentModel(models.Model):
    studentName = models.CharField(max_length=100, null=True)
    studentAddress = models.TextField(null=True)
    studentAge = models.IntegerField(null=True)
    studentRegisterdate = models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.studentName
    