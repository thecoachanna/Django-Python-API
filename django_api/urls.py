from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('authors/', views.AuthorList.as_view(), name='author_list'),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('books/', views.BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
]