from django import forms
from .models import Book, Movie, Magazine


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_name', 'language', 'genre', 'book_description', 'quantity', 'awards', 'isbn')


class MagazineForm(forms.ModelForm):
    class Meta:
        model = Magazine
        fields = ('magazine_name', 'language', 'genre', 'magazine_description', 'quantity', 'country')


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('movie_name', 'language', 'subject', 'series', 'quantity', 'movie_description')

