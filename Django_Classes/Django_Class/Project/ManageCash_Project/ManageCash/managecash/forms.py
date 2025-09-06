from django import forms
from .models import AddcashModel, ExpenceModel, CustomUserModel

class AddcashForm(forms.ModelForm):
    class Meta:
        model = AddcashModel
        fields = [ 'source',  'amount', 'description']
        widgets = {
            'source': forms.TextInput(attrs={'placeholder': 'Source', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
        }


class ExpenceForm(forms.ModelForm):
    class Meta:
        model = ExpenceModel
        fields = [ 'description', 'amount']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
        }


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ['email', 'full_name', 'address', 'phone', 'profile_picture']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }