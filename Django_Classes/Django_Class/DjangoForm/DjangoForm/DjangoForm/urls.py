from django.contrib import admin
from django.urls import path
from FormApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/',homePage,name='homePage'),
    path('',userInfoPage,name='userInfoPage'),
    path('UserInfoModelView/',UserInfoModelView,name='UserInfoModelView'),
]
