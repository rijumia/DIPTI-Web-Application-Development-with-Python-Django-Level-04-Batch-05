from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from resumeApp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home , name='home'),
    path('addDetails/', addDetails , name='addDetails'),
    path('updateDetails/<str:id>/', updateDetails , name='updateDetails'),
    path('detailsList/', detailsList, name='detailsList'),
    path('deleteResume/<str:id>/', deleteResume, name='deleteResume'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
