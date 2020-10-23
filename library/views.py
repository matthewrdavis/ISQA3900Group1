from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


def book_list(request):
    book = Book.objects.filter()
    return render(request, 'library/book_list.html',
                  {'books': book})


def book_view(request, pk):
    if pk:
        book = Book.objects.get(pk=pk)
    else:
        book = request.Book
    return render(request, 'library/book_view.html', {'books': book})

@login_required
def book_add(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            books = Book.objects.filter()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/book_add.html', {'form': form})


@login_required
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        # update
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            book = Book.objects.filter()
            return render(request, 'library/book_list.html',
                          {'books': book})
    else:
        # edit
        form = BookForm(instance=book)
    return render(request, 'library/book_edit.html', {'form': form})


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')


def magazine_list(request):
    magazine = Magazine.objects.filter()
    return render(request, 'library/magazine_list.html',
                  {'magazines': magazine})


def magazine_view(request, pk):
    if pk:
        magazine = Magazine.objects.get(pk=pk)
    else:
        magazine = request.Magazine
    return render(request, 'library/magazine_view.html', {'magazines': magazine})

@login_required
def magazine_add(request):
    if request.method == "POST":
        form = MagazineForm(request.POST)
        if form.is_valid():
            magazine = form.save(commit=False)
            magazine.save()
            return redirect('magazine_list')
    else:
        form = MagazineForm()
    return render(request, 'library/magazine_add.html', {'form': form})


@login_required
def magazine_edit(request, pk):
    magazine = get_object_or_404(Magazine, pk=pk)
    if request.method == "POST":
        # update
        form = MagazineForm(request.POST, instance=magazine)
        if form.is_valid():
            magazine = form.save(commit=False)
            magazine.save()
            magazine = Magazine.objects.filter()
            return render(request, 'library/magazine_list.html',
                          {'magazines': magazine})
    else:
        # edit
        form = MagazineForm(instance=magazine)
    return render(request, 'library/magazine_edit.html', {'form': form})


@login_required
def magazine_delete(request, pk):
    magazine = get_object_or_404(Magazine, pk=pk)
    magazine.delete()
    return redirect('magazine_list')


def movie_list(request):
    movie = Movie.objects.filter()
    return render(request, 'library/movie_list.html',
                  {'movies': movie})


def movie_view(request, pk):
    if pk:
        movie = Movie.objects.get(pk=pk)
    else:
        movie = request.Movie
    return render(request, 'library/movie_view.html', {'movies': movie})

@login_required
def movie_add(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'library/movie_add.html', {'form': form})


@login_required
def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        # update
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            movie = Movie.objects.filter()
            return render(request, 'library/movie_list.html',
                          {'movies': movie})
    else:
        # edit
        form = MovieForm(instance=movie)
    return render(request, 'library/movie_edit.html', {'form': form})


@login_required
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('movie_list')
