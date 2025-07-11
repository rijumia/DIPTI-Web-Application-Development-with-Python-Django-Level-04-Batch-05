from django.db import models

class taskModel(models.Model):
    Title=models.CharField(max_length=100)
    Description=models.TextField(max_length=200)
    Status=models.CharField(max_length=50)
    DueDate=models.DateField()
    CreatedAt=models.DateField(null=True)

    def __str__(self):
        return self.Title

