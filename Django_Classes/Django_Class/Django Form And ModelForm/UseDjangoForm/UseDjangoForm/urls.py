from django.contrib import admin
from django.urls import path
from FormsApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', DashboardPage, name='DashboardPage'),
    path('', BasicInfoView, name='BasicInfoView'),
    path('BasicInfoModelView/', BasicInfoModelView, name='BasicInfoModelView'),
    path('ViewBasicInfo/', ViewBasicInfo, name='ViewBasicInfo'),
    path('updateBasicInfo/<int:id>/', updateBasicInfo, name='updateBasicInfo'),
]
