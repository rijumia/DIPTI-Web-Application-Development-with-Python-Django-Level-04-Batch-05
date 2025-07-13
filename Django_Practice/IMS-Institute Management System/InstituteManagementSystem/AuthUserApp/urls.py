from django.urls import path
from AuthUserApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',registerPage, name='registerPage'),
    path('loginPage/',loginPage, name='loginPage'),
    path('logoutPage/',logoutPage, name='logoutPage'),
    path('changePasswordPage/',changePasswordPage, name='changePasswordPage'),
    path('profileInfoPage/',profileInfoPage, name='profileInfoPage'),

    path('homePage/',homePage, name='homePage'),

    path('teacher/register/', registerTeacherPage, name='registerTeacherPage'),
    path('teacher/teacherList/', teacherListPage, name='teacherListPage'),

    path('student/registerStudentPage/', registerStudentPage, name='registerStudentPage'),
    path('student/studentListPage/', studentListPage, name='studentListPage'),
    path('student/pendingStudentRegPage/', pendingStudentRegPage, name='pendingStudentRegPage'),
    path('student/pendingPage/', pendingPage, name='pendingPage'),
    path('student/pendingAcceptPage/<str:id>/', pendingAcceptPage, name='pendingAcceptPage'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)