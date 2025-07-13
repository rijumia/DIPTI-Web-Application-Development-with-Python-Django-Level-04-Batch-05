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



def admitedCoursePage(request):
    students = StudentModel.objects.all()
    courses = CourseModel.objects.all()

    if request.method == 'POST':
        admitted_course = request.POST.get('admitted_course')
        student = request.POST.get('student')
        payment = request.POST.get('payment')

        studentData = StudentModel.objects.get(id=student)
        courseData = CourseModel.objects.get(id=admitted_course)
        due = int(courseData.course_fee) - int(payment)

        admittedCourseData = AdmittedCourseModel.objects.create(
            student = studentData,
            admitted_course= courseData,
            course_fee = courseData.course_fee,
            payment =payment,
            due = due,
        )
        PaymentHistoryModel.objects.create(
            admitted_course = admittedCourseData,
            payment =payment,
        )
        return redirect('admittedCourseListPage')
    return render(request, 'course/admitCourse.html',{'students':students,'courses':courses})

def admittedCourseListPage(request):
    admittedCourses = AdmittedCourseModel.objects.all()
    return render(request, 'course/admittedCourse.html',{'admittedCourses':admittedCourses})


def makePaymentPage(request):
    admittedCourseData = AdmittedCourseModel.objects.all()

    if request.method == 'POST':
        admitted_course = request.POST.get('admitted_course')
        payment = request.POST.get('payment')

        admitted_course_data = AdmittedCourseModel.objects.get(id=admitted_course)

        priviewsPayment = admitted_course_data.payment
        newPayment = int(priviewsPayment) + int(payment)
        admitted_course_data.payment = newPayment

        # admitted_course_data.payment += payment
        due = admitted_course_data.course_fee - admitted_course_data.payment
        admitted_course_data.due = due

        admitted_course_data.save()

        PaymentHistoryModel.objects.create(
            admitted_course = admitted_course_data,
            payment = payment,
        )
        return redirect('admittedCourseListPage')
    return render(request, 'payment/makePayment.html',{'admittedCourseData':admittedCourseData})

def paymentHistoryPage(request):
    paymentHistories = PaymentHistoryModel.objects.all().order_by('-payment_date')
    return render(request, 'payment/paymentHistoryPage.html',{'paymentHistories':paymentHistories})
