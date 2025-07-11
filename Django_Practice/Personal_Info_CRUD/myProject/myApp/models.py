from django.db import models

class personalInfoModel(models.Model):
    Profile = models.ImageField(upload_to='Media/pic')
    Name = models.CharField(max_length=100)
    Phone = models.PositiveIntegerField()

