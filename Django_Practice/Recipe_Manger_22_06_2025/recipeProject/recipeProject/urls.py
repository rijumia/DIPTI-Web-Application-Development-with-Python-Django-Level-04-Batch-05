from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from recipeApp.views import*

urlpatterns = [
    path("admin/", admin.site.urls),
    path('home/<str:id>/',homePage, name='homePage'),
    path('recipelist/',listPage, name='listPage'),
    path('addrecipe/',addPage, name='addPage'),
    path('updaterecipe/<str:id>/',updatePage, name='updatePage'),
    path('deletePage/<str:id>/',deletePage, name='deletePage'),
    path('', loginPage, name='loginPage'),
    path('signupPage/', signinPage, name='signinPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('wrong/',wrongPage, name='wrongPage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
