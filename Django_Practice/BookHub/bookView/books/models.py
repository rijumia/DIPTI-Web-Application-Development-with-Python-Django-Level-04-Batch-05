from django.db import models

class  bookModel(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    book_price = models.DecimalField(max_digits=10, decimal_places=2)
    book_description = models.TextField()
    book_image = models.ImageField(upload_to='books/images/')

    def __str__(self):
        return self.book_name

    class Meta:
        db_table = 'book'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
