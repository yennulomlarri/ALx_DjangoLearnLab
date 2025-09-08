from .models import Book, Author, Library, Librarian

# 1. For "Query all books by a specific author" task
def books_by_author(author):
    """Query all books by a specific author"""
    return Book.objects.filter(author=author)

# 2. For "List all books in a library" task  
def books_in_library(library_name):
    """List all books in a specific library"""
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3. For "Retrieve the librarian for a library" task
def librarian_for_library(library_name):
    """Retrieve the librarian for a specific library"""
    library = Library.objects.get(name=library_name)
    return library.librarian

# 4. Alternative approaches (optional, for completeness)
def books_by_author_name(author_name):
    """Query books by author name"""
    return Book.objects.filter(author__name=author_name)

def books_in_library_filter(library):
    """List books in library using filter approach"""
    return Book.objects.filter(library=library)