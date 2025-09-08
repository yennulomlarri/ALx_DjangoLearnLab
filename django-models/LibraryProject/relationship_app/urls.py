from django.urls import path
from . import views
from .views import list_books, BookListView, LibraryDetailView, AuthorDetailView  # ← Added AuthorDetailView

urlpatterns = [
    # Function-based view - use the imported list_books function
    path('books/', list_books, name='book_list'),  # ← Changed from views.book_list to list_books
    
    # Class-based views
    path('books-class/', BookListView.as_view(), name='book_list_class'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
]