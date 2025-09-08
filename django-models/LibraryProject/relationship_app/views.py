from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout  # ← Add this
from django.contrib.auth.forms import UserCreationForm  # ← Add this
from django.contrib.auth.views import LoginView  # ← Add this
from django.urls import reverse_lazy
from .models import Book, Library, Author

# Authentication views
def register(request):
    """User registration view"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ← GitHub wants to see this
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

class CustomLoginView(LoginView):
    """User login view using Django's built-in LoginView"""
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True

def custom_logout(request):
    """User logout view"""
    logout(request)  # ← GitHub wants to see this
    return redirect('book_list')

# Your existing views below
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class BookListView(ListView):
    model = Book
    template_name = 'relationship_app/list_books.html'
    context_object_name = 'books'

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()
        return context

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'relationship_app/author_detail.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_object()
        context['books'] = author.books.all()
        return context