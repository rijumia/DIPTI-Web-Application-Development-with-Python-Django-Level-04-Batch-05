from django.contrib import admin
from django.urls import path
from bookstoreProject.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homePage, name = 'homePage'),
    path('books/', booksPage, name = 'booksPage'),
    path('user/', userPage, name = 'userPage'),
]
