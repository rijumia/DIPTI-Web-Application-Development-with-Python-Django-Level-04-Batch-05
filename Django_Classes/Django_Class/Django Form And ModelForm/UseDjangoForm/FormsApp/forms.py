from django import forms
from FormsApp.models import BasicInfoModel

class BasicInfoForm(forms.Form):
    username = forms.CharField()
    fullName = forms.CharField()
    email = forms.EmailField()
    addrees = forms.CharField()
    profileImage = forms.ImageField()

class BasicInfoModelForm(forms.ModelForm):
    class Meta:
        model = BasicInfoModel
        fields = ['username', 'fullName', 'email', 'addrees', 'profileImage']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter User Name'}),
            'fullName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'addrees': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
            'profileImage': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
