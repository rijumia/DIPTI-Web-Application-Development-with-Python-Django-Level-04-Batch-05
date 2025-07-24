from django.contrib import admin
from django.urls import path,include
from userAuthApp.urls import *
from recruiterApp.urls import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userAuthApp.urls')),
    path('', include('recruiterApp.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
