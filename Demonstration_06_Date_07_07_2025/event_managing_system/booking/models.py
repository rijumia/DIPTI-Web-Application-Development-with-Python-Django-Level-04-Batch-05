from django.db import models
from django.contrib.auth.models import AbstractUser

class EventUserModel(AbstractUser):
    full_name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField( max_length=50, null=True)
    profile_image = models.ImageField(upload_to='Media/profile', null=True)

    def __str__(self):
        return self.full_name

    
class EventBookingModel(models.Model):
     event_title = models.CharField(max_length=50, null=True)
     event_type = models.CharField(choices=[
         ('Conference', 'Conference'),
         ('Concert', 'Concert'),
         ('Wedding', 'Wedding')
     ],max_length=15, null=True)
     event_description = models.TextField(null=True)
     event_date = models.DateField(null=True)
     event_status = models.CharField(choices=[
         ('NotStarted', 'NotStarted'),
         ('InProgress', 'InProgress'),
         ('Complated', 'Complated')
     ],max_length=15, null=True)
     event_location = models.CharField(max_length=20, null=True)
     create_by = models.ForeignKey(EventUserModel, on_delete=models.CASCADE, null=True)
     created_at = models.DateTimeField(auto_now_add=True, null=True)
     updated_at = models.DateTimeField(auto_now_add=True, null=True)

     def __str__(self):
        return self.create_by
