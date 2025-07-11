from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from JobApp.models import *
from django import forms

class CustomUserForm(UserCreationForm):
    class Meta:
        model=CustomUserModel
        fields=UserCreationForm.Meta.fields+('display_name','email','user_type')
        help_texts={
            'username':None,
        }

class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model=CustomUserModel
        fields=('display_name','email',)
        help_texts={
            'username':None,
        }

class CustomUserAuthForm(AuthenticationForm):
    class Meta:
        model=CustomUserModel
        fields=['username','password']

class RecruiterForm(forms.ModelForm):
    class Meta:
        model=RecruiterModel
        fields=['company_logo','company_name','company_address']

class SeekerForm(forms.ModelForm):
    class Meta:
        model=SeekerModel
        fields=['skill_sets','resume']
        
class JobForm(forms.ModelForm):
    class Meta:
        model=JobModel
        fields=['title','number_of_openings','category','job_description','skill_sets']
        
class JobApplyForm(forms.ModelForm):
    class Meta:
        model=JobApplyModel
        fields=['skills','resume']
    
    # widgets={
    #     'resume':forms.FileInput(attrs={
    #         'type':'file'
    #     })
    # }

