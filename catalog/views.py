from django.shortcuts import render
from django.views import generic
from . models import Book, BookIntance, Author, Genre

# Create your views here.

def index(request):
    """
    View function for home page of site.
    """

    num_books = Book.objects.all().count()
    num_intance = BookIntance.objects.all().count()

    num_intance_available = BookIntance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.all().count()

    context = {
        'num_books' : num_books,
        'num_intance' : num_intance,
        'num_intance_available' : num_intance_available,
        'num_authors' : num_authors,
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author