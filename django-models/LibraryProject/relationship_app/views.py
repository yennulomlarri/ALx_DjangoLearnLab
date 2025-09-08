from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django import forms
from django.views.generic import DetailView
from .models import Book, Library

# -----------------------------
# Role check helpers
# -----------------------------
def is_admin(user):
    return user.is_superuser or user.groups.filter(name="Admin").exists()

def is_librarian(user):
    return user.groups.filter(name="Librarian").exists()

def is_member(user):
    return user.groups.filter(name="Member").exists()

# -----------------------------
# Book form
# -----------------------------
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]

# -----------------------------
# Views
# -----------------------------
@login_required
def list_books(request):
    books = Book.objects.select_related("author").all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# -----------------------------
# Restricted book management
# -----------------------------
@user_passes_test(lambda u: is_admin(u) or is_librarian(u))
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm()
    return render(request, "relationship_app/add_book.html", {"form": form})

@user_passes_test(lambda u: is_admin(u) or is_librarian(u))
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm(instance=book)
    return render(request, "relationship_app/edit_book.html", {"form": form, "book": book})

@user_passes_test(lambda u: is_admin(u) or is_librarian(u))
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "relationship_app/delete_book.html", {"book": book})

# -----------------------------
# Role-based dashboard views
# -----------------------------
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")
