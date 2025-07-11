
from django.contrib import admin
from django.urls import path
from book.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registerPage/', registerPage, name='registerPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),



    path('', home, name='home'),
    path('addBook/', addBook, name='addBook'),
    path('editBook/<str:id>', editBook, name='editBook'),
    path('viewBook/<str:id>', viewBook, name='viewBook'),
    path('deleteBook/<str:id>', deleteBook, name='deleteBook'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
