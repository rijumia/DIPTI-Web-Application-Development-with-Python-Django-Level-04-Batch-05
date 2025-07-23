from django import forms 
from JobNestApp.models import CreateJobModel

class CreateJobModelForm(forms.ModelForm):
    class Meta:
        model = CreateJobModel
        fields = ['JobTitle','description','salary','location','deadline']
        widgets = {
            'JobTitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter job title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Job description'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control mb-4', 'type': 'date'}),
        }