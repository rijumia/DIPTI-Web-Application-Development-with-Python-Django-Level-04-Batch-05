from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from LibraryApp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/',signupPage, name='signupPage'),
    path('',loginPage, name='loginPage'),
    path('changePasswordPage/',changePasswordPage, name='changePasswordPage'),
    path('logOutPage/',logOutPage, name='logOutPage'),

    path('dashboardPage/',dashboardPage, name='dashboardPage'),
    path('profilePage/',profilePage, name='profilePage'),
    path('updateProfilePage/', updateProfilePage, name='updateProfilePage'),
    
    path('bookListPage/',bookListPage, name='bookListPage'),
    path('addBookPage/',addBookPage, name='addBookPage'),
    path('books/update/<int:book_id>/', updateBookPage, name='updateBookPage'),
    path('books/delete/<int:book_id>/', deleteBookPage, name='deleteBookPage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
