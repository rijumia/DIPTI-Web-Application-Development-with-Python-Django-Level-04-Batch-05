from django.urls import path,include
from API_App.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('student-list/', studentList, name='studentList'),
    path('add-student/', addStudent, name='addStudent'),
    path('update-student/<int:pk>/', updateStudent, name='updateStudent'),
    path('delete-student/<int:pk>/', deleteStudent, name='deleteStudent'),
    path('teacher/', TeacherAPIView.as_view(), name='teacherView'),
    path('teacher-details/<int:pk>/', TeacherDetails.as_view(), name='TeacherDeatils'),
]
