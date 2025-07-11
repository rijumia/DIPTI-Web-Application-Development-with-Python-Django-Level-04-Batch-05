from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from customUsersApp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',loginPage, name='loginPage'),
    path('signup/', signupPage, name='signupPage'),
    path('logoutPage/',logoutPage, name='logoutPage'),
    path('homePage/', homePage, name='homePage'),
    path('list/', listPage, name='listPage'),
    path('deletePage/<str:id>', deletePage, name='deletePage'),
    path('view_detail/<str:id>/', view_detail, name='view_detail'),
    path('updatePage/<int:pk>/', updatePage, name='updatePage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
