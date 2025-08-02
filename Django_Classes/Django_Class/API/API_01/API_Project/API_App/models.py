from django.db import models

# Create your models here.
class StudentInfoModel(models.Model):
    StudentRoll = models.PositiveIntegerField(null=True)
    StudentUsername = models.CharField(max_length=50, null=True)
    StudentName = models.CharField(max_length=100, null=True)
    StudentAge = models.IntegerField(null=True)
    RegisterOfDate = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
<<<<<<< HEAD
        return self.StudentName
    
class TeacherModel(models.Model):
    TeacherName = models.CharField(max_length=10, null=True)
    TeacherId = models.PositiveIntegerField(null=True)
    TeacherAddress = models.TextField(null=True)
    TeacherAge = models.PositiveIntegerField(null=True)
    TeacherPic = models.ImageField(upload_to='Profile')
    
    def __str__(self):
        return self.TeacherName
=======
        return self.StudentAge
>>>>>>> 6834ddc4ec6494038c3a460856ee7b5853e7ae00
    