from django import forms 
from JobNestApp.models import CreateJobModel

class CreateJobModelForm(forms.ModelForm):
    class Meta:
        model = CreateJobModel
        fields = ['title', 'description', 'requirements', 'salary', 'location', 'job_type', 'deadline']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter job title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Job description'}),
            'requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Job requirements'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'job_type': forms.Select(attrs={'class': 'form-select'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
