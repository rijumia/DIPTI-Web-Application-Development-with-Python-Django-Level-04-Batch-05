from django import forms
from candidate_app.models import *

class JobApplyModelForm(forms.ModelForm):
    class Meta:
        model = JobApplicationModel
        fields = ['last_education','work_experience']

        widgets = {
            'last_education': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your last education'}),
            'work_experience': forms.Textarea(attrs={'class': 'form-control mb-3', 'rows': 4, 'placeholder': 'Describe your work experience'}),
        }