from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from auth_crud_app.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/', homePage, name='homePage'),
    path('', loginPage, name='loginPage'),
    path('signupPage/', signUpPage, name='signUpPage'),
    path('logOutPage/', logOutPage, name='logOutPage'),
    path('addProduct/', addProduct, name='addProduct'),
    path('listProduct/',listProduct,name='listProduct'),
    path('deletePage/<str:id>/',deletePage,name='deletePage'),
    path('updateProduct/<str:id>',updateProduct,name='updateProduct'),
    path('viewProduct/<str:id>',viewProduct,name='viewProduct'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
