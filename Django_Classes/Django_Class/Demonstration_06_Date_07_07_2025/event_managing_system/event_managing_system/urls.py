from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from booking.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',loginPage, name='loginPage'),
    path('signupPage/',signupPage, name='signupPage'),
    path('logoutPage/',logoutPage, name='logoutPage'),
    path('profilePage/',profilePage, name='profilePage'),
    path('changePasswordPage/',changePasswordPage, name='changePasswordPage'),

    path('dashboardPage/',dashboardPage, name='dashboardPage'),
    path('addBookingPage/',addBookingPage, name='addBookingPage'),
    path('myBookingPage/',myBookingPage, name='myBookingPage'),
    path('changeStatus/<str:id>/',changeStatus, name='changeStatus'),
    path('updateBookingPage/<str:id>/',updateBookingPage, name='updateBookingPage'),
    path('deleteBookingPage/<str:id>/',deleteBookingPage, name='deleteBookingPage'),
    path('viewBookingPage/<str:id>/',viewBookingPage, name='viewBookingPage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
