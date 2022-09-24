from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(
        queryset = Book.objects.all()
    )

    class Meta:
        model = Author
        fields = ('id', 'name', 'books')

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset = Author.objects.all()
    )

    class Meta:
        model = Book
        fields = ('id', 'title', 'category', 'photo_url', 'author')