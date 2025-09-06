from django.contrib import admin
from django.urls import path,include
from CalorieCounterApp.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('CalorieCounterApp.urls')),
]
