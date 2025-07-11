from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from jobProtalApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',loginPage,name='loginPage'),
    path('registerPage/',registerPage,name='registerPage'),
    path('profilePage/',profilePage,name='profilePage'),
    path('logoutPage/',logoutPage,name='logoutPage'),
    
    path('homePage/',homePage,name='homePage'),
    path('jobFeedPage/',jobFeedPage,name='jobFeedPage'),
    path('addJobPage/',addJobPage,name='addJobPage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
