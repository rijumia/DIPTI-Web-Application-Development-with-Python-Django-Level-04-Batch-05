from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from books.views import home, all_books, add_book, update_book, delete_book, view_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('allbooks/', all_books, name='all_books'),
    path('addbook/', add_book, name='add_book'),
    path('updatebook/<str:id>/', update_book, name='update_book'),
    path('deletebook/<str:id>/', delete_book, name='delete_book'),
    path('viewbook/<str:id>/', view_book, name='view_book'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
