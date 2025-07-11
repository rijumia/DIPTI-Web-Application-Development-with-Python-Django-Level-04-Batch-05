from django.db import models

# Create your models here.
class studentModel(models.Model):
    profile_image = models.ImageField(upload_to='media/images')
    name =models.CharField(max_length=100)
    roll_number =models.IntegerField()
    email =models.EmailField()
    phone =models.CharField(max_length=17)
    address =models.TextField()
    dob=models.DateField()
    is_active=models.BooleanField(default=True)
