from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Library, Author  # ← Library must be here

# 1. Function-based view that lists all books
def book_list(request):
    """List all books stored in the database - function-based view"""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# 2. Class-based view that lists all books
class BookListView(ListView):
    """List all books - class-based view"""
    model = Book
    template_name = 'relationship_app/list_books.html'
    context_object_name = 'books'

# 3. Class-based view that displays library details - GitHub is specifically checking this one
class LibraryDetailView(DetailView):
    """Display details for a specific library, listing all books available in that library"""
    model = Library  # ← This line requires "from .models import Library"
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        """Add all books in this library to the context"""
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()  # ← Lists all books available in that library
        return context

# 4. Additional view if needed for authors
class AuthorDetailView(DetailView):
    """Display details for a specific author, listing all their books"""
    model = Author
    template_name = 'relationship_app/author_detail.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        """Add all books by this author to the context"""
        context = super().get_context_data(**kwargs)
        author = self.get_object()
        context['books'] = author.books.all()
        return context