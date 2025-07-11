from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')
def addBooks(request):
    return render(request, 'add-books.html')
def addStudent(request):
    return render(request, 'add-student.html')
def addDepartment(request):
    return render(request, 'add-department.html')
def addEvents(request):
    return render(request, 'add-events.html')
def addExam(request):
    return render(request, 'add-exam.html')
def addExpenses(request):
    return render(request, 'add-expenses.html')
def addFeesCollection(request):
    return render(request, 'add-fees-collection.html')
def addFees(request):
    return render(request, 'add-fees.html')
def addHoliday(request):
    return render(request, 'add-holiday.html')
def addRoom(request):
    return render(request, 'add-room.html')
def addSalary(request):
    return render(request, 'add-salary.html')
def addSports(request):
    return render(request, 'add-sports.html')
def addSubject(request):
    return render(request, 'add-subject.html')
def addTeacher(request):
    return render(request, 'add-teacher.html')
def addTimeTable(request):
    return render(request, 'add-time-table.html')
def addTransport(request):
    return render(request, 'add-transport.html')


def teacherDashboard(request):
    return render(request, 'teacher-dashboard.html')
def studentDashboard(request):
    return render(request, 'student-dashboard.html')
def students(request):
    return render(request, 'students.html')
def studentDetails(request):
    return render(request, 'student-details.html')
def editStudent(request):
    return render(request, 'edit-student.html')
def teachers(request):
    return render(request, 'teachers.html')
def teacherDetails(request):
    return render(request, 'teacher-details.html')
def editTeacher(request):
    return render(request, 'edit-teacher.html')
