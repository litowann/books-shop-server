from django.urls import path
from .views import books_list

urlpatterns = [
    path('books/', books_list, name="books_list")
]
