from django.db import models

class BooksModel(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    book_file = models.FileField(upload_to='books/')
    cover_image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

