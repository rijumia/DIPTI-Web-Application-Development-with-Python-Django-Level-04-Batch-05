from django.contrib import admin
from django.urls import path
from userAuth.views import registration, login, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', registration, name='registration'),
    path('', login, name='login'),
    path('home/', home, name='home'),
]
