from django.contrib import admin
from django.urls import path
from portfolioApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Authentication
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

    # Dashboard
    path('dashboard/', dashboard_view, name='dashboard'),

    # Skill URLs
    path('skill/add/', skill_add, name='skill_add'),
    path('skill/<int:pk>/edit/', skill_edit, name='skill_edit'),
    path('skill/<int:pk>/delete/', skill_delete, name='skill_delete'),

    # Project URLs
    path('project/add/', project_add, name='project_add'),
    path('project/<int:pk>/edit/', project_edit, name='project_edit'),
    path('project/<int:pk>/delete/', project_delete, name='project_delete'),

    # Work Experience URLs
    path('work/add/', work_add, name='work_add'),
    path('work/<int:pk>/edit/', work_edit, name='work_edit'),
    path('work/<int:pk>/delete/', work_delete, name='work_delete'),

    # Education URLs
    path('education/add/', education_add, name='education_add'),
    path('education/<int:pk>/edit/', education_edit, name='education_edit'),
    path('education/<int:pk>/delete/', education_delete, name='education_delete'),

    # Public portfolio and resume
    path('portfolio/<str:username>/', portfolio_view, name='portfolio'),
    path('portfolio/', portfolio_view, name='portfolio_default'),

    path('resume/<str:username>/', resume_view, name='resume'),
    path('resume/', resume_view, name='resume_default'),

    # Contact
    path('contact/', contact_view, name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
