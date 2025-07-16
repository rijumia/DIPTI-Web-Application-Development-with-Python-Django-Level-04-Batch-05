from django import forms
from .models import TeacherModel

class AddTeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherModel
        fields = ['teacherName', 'lastEducation', 'phone', 'address']
        widgets = {
            'teacherName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter teacher name'}),
            'lastEducation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last education'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Address'}),
        }
