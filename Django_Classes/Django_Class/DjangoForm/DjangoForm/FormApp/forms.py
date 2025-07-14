from django import forms

class UserInfoForm(forms.Form):
    FullName = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.IntegerField()
    addrees = forms.CharField(max_length=50)