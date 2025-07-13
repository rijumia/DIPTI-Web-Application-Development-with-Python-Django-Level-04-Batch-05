from django.shortcuts import render,redirect
from Course_App.models import*

# Create your views here.
def createCoursePage(request):
    teacherData= TeacherModel.objects.all()
    if request.method == 'POST':
        course_title = request.POST.get('course_title')
        course_description = request.POST.get('course_description')
        course_duration = request.POST.get('course_duration')
        course_start_date = request.POST.get('course_start_date')
        course_fee = request.POST.get('course_fee')
        assign_teacher = request.POST.get('assign_teacher')
        teacher = TeacherModel.objects.get(id=assign_teacher)

        CourseModel.objects.create(
            course_title = course_title,
            course_description = course_description,
            course_duration = course_duration,
            course_start_date = course_start_date,
            course_fee = course_fee,
            assign_teacher = teacher,
        )
        return redirect('allCoursePage')
    return render(request, 'course/createCourse.html',{'teacherData':teacherData})

def allCoursePage(request):
    courses = CourseModel.objects.all()
    return render(request, 'course/allCourse.html',{'courses':courses})



def admittedCoursePage(request):
    
    return render(request, 'course/admittedCourse.html')
