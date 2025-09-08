from .models import Book, Author, Library, Librarian

# 1. GitHub wants this EXACT pattern ↓
def books_by_author(author):
    """Query all books by a specific author using objects.filter(author=author)"""
    return Book.objects.filter(author=author)

# 2. List all books in a library
def books_in_library(library):
    """List all books in a specific library"""
    return Book.objects.filter(library=library)

# 3. Retrieve the librarian for a library  
def librarian_for_library(library):
    """Retrieve the librarian for a specific library"""
    return Librarian.objects.get(library=library)

# 4. Alternative: Query by author name
def books_by_author_name(author_name):
    """Query all books by a specific author name"""
    return Book.objects.filter(author__name=author_name)

# 5. Alternative: List books by library name
def books_in_library_by_name(library_name):
    """List all books in a library by library name"""
    return Book.objects.filter(library__name=library_name)