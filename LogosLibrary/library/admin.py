from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Book, Magazine, Movie


class BookList(admin.ModelAdmin):
   list_display = ('book_name', 'genre', 'isbn')
   list_filter = ('book_name', 'genre', 'isbn')
   search_fields = ('book_name',)
   ordering = ['book_name']


class MagazineList(admin.ModelAdmin):
   list_display = ('magazine_name', 'genre')
   list_filter = ('magazine_name', 'genre')
   search_fields = ('magazine_name',)
   ordering = ['magazine_name']


class MovieList(admin.ModelAdmin):
   list_display = ('movie_name', 'subject', 'series')
   list_filter = ('movie_name', 'series', 'subject')
   search_fields = ('movie_name',)
   ordering = ['movie_name']


admin.site.register(Book, BookList)
admin.site.register(Magazine, MagazineList)
admin.site.register(Movie, MovieList)
