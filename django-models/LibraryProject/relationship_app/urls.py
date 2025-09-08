from django.urls import path
from . import views
from .views import list_books, BookListView, LibraryDetailView, AuthorDetailView, CustomLoginView, register, custom_logout

urlpatterns = [
    # Authentication URLs
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
    
    # Your existing URLs
    path('books/', list_books, name='book_list'),
    path('books-class/', BookListView.as_view(), name='book_list_class'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
]