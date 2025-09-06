from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Skill, Project, WorkExperience, Education, ContactMessage

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username or Email')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            # override to allow login by email or username
            user_queryset = CustomUser.objects.filter(username=username)
            if not user_queryset.exists():
                # try filtering by email
                user_queryset = CustomUser.objects.filter(email=username)
                if user_queryset.exists():
                    username = user_queryset.first().username
                    self.cleaned_data['username'] = username
        return super().clean()

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

# CRUD forms for Portfolio models (simple ModelForms)
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'proficiency']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'url', 'image']

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['position', 'company', 'description', 'start_date', 'end_date', 'currently_working']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'degree', 'field_of_study', 'start_date', 'end_date', 'description']