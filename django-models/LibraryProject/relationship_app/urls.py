from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books, BookListView, LibraryDetailView, AuthorDetailView

urlpatterns = [
    # Authentication URLs (EXACT patterns GitHub wants)
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),
    
    # Your existing URLs
    path('books/', list_books, name='book_list'),
    path('books-class/', BookListView.as_view(), name='book_list_class'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
]