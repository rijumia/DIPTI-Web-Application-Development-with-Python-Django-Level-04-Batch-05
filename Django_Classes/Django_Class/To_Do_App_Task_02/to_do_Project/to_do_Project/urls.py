from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from to_do_App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginPage, name='loginPage'),
    path('registerPage/', registerPage, name='registerPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('changePassword/', changePassword, name='changePassword'),

    path('homePage', homePage, name='homePage'),
    path('addToDo/', addToDo, name='addToDo'),
    path('listToDo/', listToDo, name='listToDo'),
    path('viewToDo/<str:id>/', viewToDo, name='viewToDo'),
    path('editToDo/<str:id>/', editToDo, name='editToDo'),
    path('deleteToDo/<str:id>/', deleteToDo, name='deleteToDo'),

    path('error/', custom_error, name='custom_error'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
