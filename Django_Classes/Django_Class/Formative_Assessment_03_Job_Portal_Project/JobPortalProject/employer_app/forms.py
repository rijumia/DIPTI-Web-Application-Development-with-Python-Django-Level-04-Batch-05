from django import forms
from employer_app.models import JobModel

class JobModelForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = ['title','description','requirements','salary','job_type','deadline']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter job title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Job description',
                'rows': 4
            }),
            'requirements': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Job requirements',
                'rows': 4
            }),
            'salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter salary amount'
            }),
            'job_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'deadline': forms.DateInput(attrs={
                'class': 'form-control mb-3',
                'type': 'date'
            }),
        }