from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from books.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('bookList', bookList, name='bookList'),
    path('book_add', bookForm, name='bookAdd'),
    path('book_update/<str:id>/', bookUpdate, name='bookUpdate'),
    path('bookList/<str:id>/', bookDelete, name='bookDelete'),
    path('view/<str:id>/', viewBook, name='viewBook')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
