from django.contrib import admin
from .models import UserProfile, Job, JobApplication

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_type', 'display_name']
    list_filter = ['user_type']
    search_fields = ['user__username', 'display_name']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'recruiter', 'category', 'number_of_openings', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'description']

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['job', 'applicant', 'applied_at']
    list_filter = ['applied_at']
    search_fields = ['job__title', 'applicant__user__username']
