#!/usr/bin/env python3
import os
import django
import sys

# Add the project root directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    """Create sample data for testing relationships"""
    print("Creating sample data...")
    
    # Create authors
    author1, created = Author.objects.get_or_create(name="J.K. Rowling")
    author2, created = Author.objects.get_or_create(name="George R.R. Martin")
    author3, created = Author.objects.get_or_create(name="Stephen King")
    
    # Create books
    book1, created = Book.objects.get_or_create(
        title="Harry Potter and the Philosopher's Stone", 
        author=author1, 
        publication_year=1997
    )
    book2, created = Book.objects.get_or_create(
        title="A Game of Thrones", 
        author=author2, 
        publication_year=1996
    )
    book3, created = Book.objects.get_or_create(
        title="The Shining", 
        author=author3, 
        publication_year=1977
    )
    book4, created = Book.objects.get_or_create(
        title="Harry Potter and the Chamber of Secrets", 
        author=author1, 
        publication_year=1998
    )
    
    # Create libraries
    library1, created = Library.objects.get_or_create(name="Central Library")
    library2, created = Library.objects.get_or_create(name="City Public Library")
    
    # Add books to libraries
    library1.books.add(book1, book2, book3)
    library2.books.add(book1, book4)
    
    # Create librarians
    librarian1, created = Librarian.objects.get_or_create(
        name="Sarah Johnson", 
        library=library1
    )
    librarian2, created = Librarian.objects.get_or_create(
        name="Michael Brown", 
        library=library2
    )
    
    print("Sample data created successfully!")
    return author1, library1

def query_samples():
    """Demonstrate the required queries from Task 0"""
    print("\n" + "="*50)
    print("DEMONSTRATING QUERIES FROM TASK 0")
    print("="*50)
    
    # Create sample data first
    author, library = create_sample_data()
    
    # 1. Query all books by a specific author
    print("\n1. Query all books by a specific author:")
    print(f"Books by {author.name}:")
    books_by_author = Book.objects.filter(author=author)
    for book in books_by_author:
        print(f"  - {book.title} ({book.publication_year})")
    
    # 2. List all books in a library
    print(f"\n2. List all books in {library.name}:")
    books_in_library = library.books.all()
    for book in books_in_library:
        print(f"  - {book.title} by {book.author.name}")
    
    # 3. Retrieve the librarian for a library
    print(f"\n3. Retrieve the librarian for {library.name}:")
    try:
        librarian = Librarian.objects.get(library=library)
        print(f"  Librarian: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"  No librarian found for {library.name}")
    
    print("\n" + "="*50)
    print("QUERY DEMONSTRATION COMPLETE")
    print("="*50)

if __name__ == "__main__":
    query_samples()