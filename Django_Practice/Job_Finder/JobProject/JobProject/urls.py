from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from JobApp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginPage, name='loginPage'),
    path('register/', signupPage, name='signupPage'),
    path('changePassword/', changePasswordPage, name='changePasswordPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),

    path('profile/', profilePage, name='profilePage'),    

    path('homePage/', homePage, name='homePage'),
    path('jobFeedPage/', jobFeedPage, name='jobFeedPage'),
    path('addJobPage/', addJobPage, name='addJobPage'),
    path('jobViewPage/<str:id>/', jobViewPage, name='jobViewPage'),
    path('jobEditPage/<str:id>/', jobEditPage, name='jobEditPage'),
    path('jobDeletePage/<str:id>/', jobDeletePage, name='jobDeletePage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
