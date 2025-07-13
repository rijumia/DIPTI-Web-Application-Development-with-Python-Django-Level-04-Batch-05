from django.shortcuts import render,redirect
from courses.models import *

# Create your views here.

def addCourse(request):
    teachers = TeacherModel.objects.all()

    if request.method == 'POST':
        CourseModel.objects.create(
            course_title = request.POST.get('course_title'),
            course_description = request.POST.get('course_description'),
            course_duration = request.POST.get('course_duration'),
            course_start_date = request.POST.get('course_start_date'),
            course_fee = request.POST.get('course_fee'),
            assign_teacher_id = request.POST.get('assign_teacher'),
        )
        return redirect('course')  # update with your correct name

    return render(request, 'courses/addCourse.html', {
        'teacher_list': teachers
    })


def course(request):
    courses = CourseModel.objects.select_related('assign_teacher').all()
    return render(request, 'courses/course.html', {'courses': courses})