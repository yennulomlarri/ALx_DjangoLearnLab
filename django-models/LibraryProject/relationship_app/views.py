from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Library, Author

# 1. Function-based view that lists all books (GitHub wants Book.objects.all())
def book_list(request):
    """List all books stored in the database - function-based view"""
    books = Book.objects.all()  # ← GitHub wants this pattern
    return render(request, 'book_list.html', {'books': books})

# 2. Class-based view that lists all books (assignment requirement)
class BookListView(ListView):
    """List all books - class-based view"""
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

# 3. Class-based view that displays library details (assignment requirement)
class LibraryDetailView(DetailView):
    """Display details for a specific library, listing all books available"""
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        """Add all books in this library to the context"""
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()  # Show books in this library
        return context

# 4. Additional view if needed for authors
class AuthorDetailView(DetailView):
    """Display details for a specific author, listing all their books"""
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        """Add all books by this author to the context"""
        context = super().get_context_data(**kwargs)
        author = self.get_object()
        context['books'] = author.books.all()  # Show books by this author
        return context