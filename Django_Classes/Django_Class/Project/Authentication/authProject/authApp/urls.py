from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', loginPage, name='loginPage'),
    path('register/', register, name='register'),
    path('changePassword/', changePassword, name='changePassword'),
    path('log-out/', logoutPage, name='logoutPage'),

    path('profile/', profile, name='profile'),
    path('update-profile/', updateProfile, name='updateProfile'),

    path('dashboard/', dashboard, name='dashboard'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
