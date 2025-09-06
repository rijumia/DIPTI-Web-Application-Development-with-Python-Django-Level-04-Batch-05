from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['fullName','phone','profilePhoto']

        widgets = {
            'fullName': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'profilePhoto': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }