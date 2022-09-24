from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    photo_url = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

   