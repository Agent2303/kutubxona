from django.db import models
from django.contrib.auth.models import User
from books.models import BooksModel

class CommentsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BooksModel, on_delete=models.CASCADE)
    comment_text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book
    


# class DownloadModel(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     book = models.ForeignKey(BooksModel,on_delete=models.CASCADE)
#     date_downloaded = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.book