from django.db import models
from users_auth_app.models import*

# Create your models here.
class CandidateProfileModel(models.Model):
    candidate_user = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='candidate_profile',null=True)
    full_name = models.CharField(max_length=255,null=True)
    phone = models.CharField(max_length=20,null=True)
    email = models.EmailField(null=True)
    address = models.TextField(blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.full_name