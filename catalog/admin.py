from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookIntance,Language

#admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
#admin.site.register(Author)
#admin.site.register(BookIntance)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]



class BookIntanceInLine(admin.TabularInline):
    model = BookIntance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookIntanceInLine]

@admin.register(BookIntance)
class BookIntanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {'fields' :
                    ('book', 'imprint', 'id')}),
        ('Availability', {'fields' :
                              ('status', 'due_back')}),
    )
