from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    book_description = models.TextField()
    quantity = models.IntegerField()
    awards = models.TextField()
    isbn = models.IntegerField()


class Magazine(models.Model):
    magazine_name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    magazine_description = models.TextField()
    quantity = models.IntegerField()
    country = models.CharField(max_length=100)


class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    series = models.TextField()
    quantity = models.IntegerField()
    movie_description = models.TextField()
