from django.db import models

class studentModel(models.Model):
    StudentName = models.CharField(max_length=50)
    StudentRoll = models.PositiveIntegerField()
    StudentDepartment = models.CharField(max_length=100)
    StudentImage = models.ImageField(upload_to='Student/img')
    create_at = models.DateTimeField(auto_now_add=True)
    
class todoModel(models.Model):
    TodoTitle = models.CharField(max_length=50)
    TodoDescription = models.CharField(max_length=100)
    TodoStatus = models.CharField()
    TodoDueDate = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)