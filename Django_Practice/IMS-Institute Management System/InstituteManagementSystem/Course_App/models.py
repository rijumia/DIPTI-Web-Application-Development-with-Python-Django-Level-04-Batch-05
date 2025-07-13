from django.db import models
from AuthUserApp.models import TeacherModel, StudentModel


class CourseModel(models.Model):
    course_title = models.CharField(max_length=100, null=True)
    course_description = models.TextField(null=True)
    course_duration = models.CharField(max_length=100, null=True)
    course_start_date = models.DateField(null=True)
    course_fee = models.PositiveIntegerField(null=True)
    assign_teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE,  null=True, related_name='courseTeacher_info')


class AdmittedCourseModel(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE, null=True, related_name='studentCourse_info')
    admitted_course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, null=True, related_name='studentCourse_info')
    course_fee = models.PositiveIntegerField(null=True)
    payment = models.PositiveIntegerField(null=True)
    due = models.PositiveIntegerField(null=True)
    admitted_date = models.DateTimeField(auto_now_add=True,null=True)

class PaymentHistoryModel(models.Model):
    admitted_course = models.ForeignKey(AdmittedCourseModel, on_delete=models.CASCADE, null=True, related_name='paymentCourse_info')
    payment = models.PositiveIntegerField(null=True)
    due = models.PositiveIntegerField(null=True)
    payment_date = models.DateTimeField(auto_now_add=True,null=True)
