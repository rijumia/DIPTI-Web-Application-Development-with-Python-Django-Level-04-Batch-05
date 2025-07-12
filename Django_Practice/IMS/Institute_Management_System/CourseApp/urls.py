from django.urls import path
from .views import createCoursePage, coursePage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('createCoursePage/', createCoursePage, name='createCoursePage'),
    path('coursePage/', coursePage, name='coursePage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)