from django.db import models

class studentModel(models.Model):
    Student_Name=models.CharField(max_length=100)
    Student_Department=models.CharField(max_length=100)
    Student_City=models.CharField(max_length=100)
    Student_Age=models.IntegerField()
    
class teacherModel(models.Model):
    Teacher_Name=models.CharField(max_length=100)
    Teacher_Subject=models.CharField(max_length=50)
    Teacher_email=models.EmailField()
    Teacher_phone=models.IntegerField(max_length=11)
    Teacher_department=models.CharField(max_length=100)
    
class courseModel(models.Model):
    Course_Name=models.CharField(max_length=100)
    Course_Code=models.IntegerField(max_length=9)
    Course_Instructor=models.CharField()
    Course_Credits=models.IntegerField(max_length=9)
    Course_Description=models.TextField(max_length=200)