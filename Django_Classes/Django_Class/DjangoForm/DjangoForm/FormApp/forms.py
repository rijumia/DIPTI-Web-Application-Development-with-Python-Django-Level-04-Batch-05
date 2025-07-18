from django import forms
from FormApp.models import UserInfoModelsTwo

class UserInfoForm(forms.Form):
    FullName = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your full name'
        })
    )
    email = forms.EmailField()
    phone = forms.IntegerField()
    addrees = forms.CharField(max_length=50)
    image = forms.ImageField()
    
class UserInfoModelFormTwo(forms.ModelForm):
    class Meta:
        model = UserInfoModelsTwo
        fields = ['FullName','email','phone','addrees','image']