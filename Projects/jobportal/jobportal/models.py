from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class UserProfile(models.Model):
    USER_TYPES = [
        ('recruiter', 'Recruiter'),
        ('jobseeker', 'Job Seeker'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    

    company_name = models.CharField(max_length=200, blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    company_website = models.URLField(blank=True, null=True)
    

    skills = models.TextField(blank=True, null=True, help_text="Enter skills separated by commas")
    resume = models.FileField(
        upload_to='resumes/', 
        blank=True, 
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.display_name} ({self.user_type})"
    
    def get_skills_list(self):
        if self.skills:
            return [skill.strip().lower() for skill in self.skills.split(',')]
        return []

class Job(models.Model):
    CATEGORY_CHOICES = [
        ('technology', 'Technology'),
        ('finance', 'Finance'),
        ('healthcare', 'Healthcare'),
        ('education', 'Education'),
        ('marketing', 'Marketing'),
        ('sales', 'Sales'),
        ('other', 'Other'),
    ]
    
    recruiter = models.ForeignKey(UserProfile, on_delete=models.CASCADE, limit_choices_to={'user_type': 'recruiter'})
    title = models.CharField(max_length=200)
    number_of_openings = models.PositiveIntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    required_skills = models.TextField(help_text="Enter required skills separated by commas")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_required_skills_list(self):
        if self.required_skills:
            return [skill.strip().lower() for skill in self.required_skills.split(',')]
        return []

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(UserProfile, on_delete=models.CASCADE, limit_choices_to={'user_type': 'jobseeker'})
    applied_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['job', 'applicant']
    
    def __str__(self):
        return f"{self.applicant.display_name} applied for {self.job.title}"
