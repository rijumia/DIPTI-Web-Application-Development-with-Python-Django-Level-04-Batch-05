from django import forms
from CRUDapp.models import *

class CompanyModelForm(forms.ModelForm):
    class Meta:
        model = CompanyModel
        fields = '__all__'

class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = '__all__'


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'


class JobModelForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = ['title', 'designation', 'salary','deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        }