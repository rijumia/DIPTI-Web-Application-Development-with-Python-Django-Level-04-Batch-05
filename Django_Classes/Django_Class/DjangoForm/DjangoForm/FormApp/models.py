from django.db import models

# Create your models here.
class UserInfoModels(models.Model):
    FullName = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=True)
    phone = models.IntegerField(null=True)
    addrees = models.CharField(max_length=50,null=True)
    image = models.ImageField(null=True)
    
    def __str__(self):
        return self.email
    
class UserInfoModelsTwo(models.Model):
    FullName = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=True)
    phone = models.IntegerField(null=True)
    addrees = models.CharField(max_length=50,null=True)
    image = models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.FullName