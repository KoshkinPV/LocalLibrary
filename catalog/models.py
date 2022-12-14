from django.db import models
from django.urls import reverse
import uuid
# Create your models here.

class Genre(models.Model):
    """
    Model representing a book genre
    """

    name = models.CharField(max_length=200, help_text="Enter a book ganre: ")
    """
    String for representing the Model object 
    """
    def __str__(self):
        return self.name

class Language(models.Model):
    """
    Model representing a language of a book.
    """

    name = models.CharField(max_length=200, help_text="Enter a book language: ")

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model representing a Book
    """

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    """
    ForeignKey used because book can have only one author, but author can have a lot of books.
    
    Author as a string rather than object because it hasn't been declared yet in file yet.
    """

    summary = models.CharField(max_length=1000, help_text="Enter a brief description of the book")

    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character '
        '"<ahref="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    """
    ManyToManyField used because genre can contain a many book, and books also can contain a many genre
    
    Genre class has already been declared so we can specify rhe object above.
    """

    def display_genre(self):
        """
        Create a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookIntance(models.Model):
    """
    Model representing a specific copu of a book
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular"
                                                                          " book across whole library")

    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text="Book availability")

    class Meta:
        ordering = ["due_back"]


    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id, self.book.title)


class Author(models.Model):
    """
    Model representing an author.
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """

        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object
        """

        return '%s, %s' % (self.last_name, self.first_name)

