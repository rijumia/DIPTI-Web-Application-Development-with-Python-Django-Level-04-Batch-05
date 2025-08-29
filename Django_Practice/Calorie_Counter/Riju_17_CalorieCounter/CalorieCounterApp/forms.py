from django import forms
from .models import *

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ['name','age','gender','height','weight']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Height (cm)'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Weight (kg)'}),
        }

class DailyConsumedForm(forms.ModelForm):
    class Meta:
        fields = ['itemName','calories','date']
        widgets = {
            'itemName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item Name'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Calories'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }