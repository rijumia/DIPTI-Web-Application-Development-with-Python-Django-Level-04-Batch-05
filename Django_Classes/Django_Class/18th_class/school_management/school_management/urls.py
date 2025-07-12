
from django.contrib import admin
from django.urls import path
from school.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('add-books/', addBooks, name='addBooks'),
    path('add-Student/', addStudent, name='addStudent'),
    path('add-Department/', addDepartment, name='addDepartment'),
    path('add-Events/', addEvents, name='addEvents'),
    path('add-Exam/', addExam, name='addExam'),
    path('add-Expenses/', addExpenses, name='addExpenses'),
    path('add-FeesCollection/', addFeesCollection, name='addFeesCollection'),
    path('add-Fees/', addFees, name='addFees'),
    path('add-Holiday/', addHoliday, name='addHoliday'),
    path('add-Room/', addRoom, name='addRoom'),
    path('add-Salary/', addSalary, name='addSalary'),
    path('add-Sports/', addSports, name='addSports'),
    path('add-Subject/', addSubject, name='addSubject'),
    path('add-Teacher/', addTeacher, name='addTeacher'),
    path('add-TimeTable/', addTimeTable, name='addTimeTable'),
    path('add-Transport/', addTransport, name='addTransport'),


    path('teacher-Dashboard/', teacherDashboard, name='teacherDashboard'),
    path('student-Dashboard/', studentDashboard, name='studentDashboard'),
    path('students/', students, name='students'),
    path('studentDetails/', studentDetails, name='studentDetails'),
    path('editStudent/', editStudent, name='editStudent'),
    path('teachers/', teachers, name='teachers'),
    path('teacherDetails/', teacherDetails, name='teacherDetails'),
    path('editTeacher/', editTeacher, name='editTeacher'),
   
]
