from django.urls import path
from .views import *



urlpatterns = [
    path('books/', get_books),
    path('books-create/', create_books),
    path('books/<int:pk>/', get_books_by_id),
    path('books-update/<int:pk>/', update_books),
    path('books-delete/<int:pk>/', delete_books)
]