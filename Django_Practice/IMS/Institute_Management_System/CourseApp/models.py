from django.db import models
from UserAuthApp.models import TeacherModel, StudentModel


class CourseModel(models.Model):
    course_title = models.CharField(max_length=100,null=True)
    course_description = models.TextField(null=True)    
    course_duration = models.CharField(max_length=20,null=True)
    course_Start_date = models.DateField(null=True)
    course_fee = models.PositiveIntegerField(null=True)
    assign_course = models.ForeignKey(TeacherModel,on_delete=models.CASCADE, null=True, related_name='assign_teacher')

    def __str__(self):
        return self.course_title
    
class AdmittedCourseModel(models.Model):
    student = models.ForeignKey(StudentModel,on_delete=models.CASCADE, null=True, related_name='admitted_student')
    admitted_course = models.ForeignKey(CourseModel,on_delete=models.CASCADE, null=True, related_name='admitted_course')
    course_fee = models.PositiveIntegerField(null=True)
    payment = models.PositiveIntegerField(null=True)
    due = models.PositiveIntegerField(null=True)
    admitted_date =  models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.student
    
class PaymentHistoryModel(models.Model):
    student = models.ForeignKey(StudentModel,on_delete=models.CASCADE, null=True, related_name='admitted_student_payment')
    admitted_course = models.ForeignKey(CourseModel,on_delete=models.CASCADE, null=True, related_name='admitted_course_payment')
    payment = models.PositiveIntegerField(null=True)
    payment_date =  models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.student