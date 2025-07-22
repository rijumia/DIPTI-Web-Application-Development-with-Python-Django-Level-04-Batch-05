from django import forms
from candidate_app.models import *

class JobApplyModelForm(forms.ModelForm):
    class Meta:
        model = JobApplicationModel
        fields = ['last_education','work_experience']