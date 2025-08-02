from django.contrib import admin
from django.urls import path, include
from API_App.urls import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('API_App.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
