
from django.contrib import admin
from django.urls import path
from newsApp.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # --------------Authentication-------------------->
    path('registerPage/', registerPage, name='registerPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),

    # ---------------CRUD--------------------------->
    path('', home, name='home'),
    path('addNews/', addNews, name='addNews'),
    path('editNews/<str:id>', editNews, name='editNews'),
    path('viewNews/<str:id>', viewNews, name='viewNews'),
    path('deleteNews/<str:id>', deleteNews, name='deleteNews'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
