from django.urls import path
from userAuthApp.views import *


urlpatterns = [
    path('', registerPage, name='registerPage'),
    path('login/', loginPage, name='loginPage'),
    path('logout/', logoutPage, name='logoutPage'),
    path('changePassword/', changePassword, name='changePassword'),
    
    path('homePage/', homePage, name='homePage'),

    path('dashboard-recruiter/', dashboardRecruiterPage, name='dashboardRecruiterPage'),
    path('dashboard-seeker/', dashboardSeekerPage, name='dashboardSeekerPage'),
]