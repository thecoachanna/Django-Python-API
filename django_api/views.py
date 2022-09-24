from django.shortcuts import render

# Create your views here.
from .models import Author, Book
from django.http import JsonResponse
from rest_framework import generics
from .serializers import AuthorSerializer, BookSerializer

# Author Views
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()


# Book Views
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = AuthorSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()