from django.urls import path
from . import views
from .views import BookListView, LibraryDetailView, AuthorDetailView

urlpatterns = [
    # Function-based view (for GitHub check)
    path('books/', views.book_list, name='book_list'),
    
    # Class-based views (for assignment)
    path('books-class/', BookListView.as_view(), name='book_list_class'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
]