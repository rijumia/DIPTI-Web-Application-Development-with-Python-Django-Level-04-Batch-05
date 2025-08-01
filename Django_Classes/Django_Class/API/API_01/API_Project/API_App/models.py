from django.db import models

# Create your models here.
class StudentInfoModel(models.Model):
    StudentRoll = models.PositiveIntegerField(null=True)
    StudentUsername = models.CharField(max_length=50, null=True)
    StudentName = models.CharField(max_length=100, null=True)
    StudentAge = models.IntegerField(null=True)
    RegisterOfDate = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.StudentAge
    