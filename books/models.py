from django.db import models
from django.utils import timezone

from users.models import CustomUser


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    isbn = models.CharField(max_length=17)
    author = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title


class BookReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment
