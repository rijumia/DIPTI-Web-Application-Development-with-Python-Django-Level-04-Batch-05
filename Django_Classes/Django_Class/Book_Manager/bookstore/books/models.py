from django.db import models

class booksModel(models.Model):
    BookTitle = models.CharField(max_length=50, null=True)
    BookAuthor = models.CharField(max_length=50, null=True)
    BookCategory = models.CharField(max_length=100, null=True)
    BookPublishDate = models.DateField(auto_now_add=True, null=True)
    BookDescription = models.TextField(null=True)
    BookCoverPhoto = models.ImageField(upload_to='Media/cover_photo', null=True)
