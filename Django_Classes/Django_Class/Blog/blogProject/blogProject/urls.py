from django.contrib import admin
from django.urls import path
from blogProject.views import homePage, blogPage, userPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='homePage'),
    path('blog/', blogPage, name='blogPage'),
    path('user/', userPage, name='userPage')
]
