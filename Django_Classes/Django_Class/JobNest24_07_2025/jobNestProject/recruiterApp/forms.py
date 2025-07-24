from django import forms 
from recruiterApp.models import RecruiterProfileModel


class RecruiterProfileModelForm(forms.ModelForm):
    class Meta:
        model = RecruiterProfileModel
        fields = ['company_name', 'email', 'phone', 'about_company', 'company_logo', 'location']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'about_company': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'About company', 'rows': 4}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
        }

