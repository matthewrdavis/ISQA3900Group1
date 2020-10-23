from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'library'
urlpatterns = [
    path('book/add/', views.book_add, name='book_add'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('magazine/add/', views.magazine_add, name='magazine_add'),
    path('magazine/<int:pk>/edit/', views.magazine_edit, name='magazine_edit'),
    path('magazine/<int:pk>/delete/', views.magazine_delete, name='magazine_delete'),
    path('movie/add/', views.movie_add, name='movie_add'),
    path('movie/<int:pk>/edit/', views.movie_edit, name='movie_edit'),
    path('movie/<int:pk>/delete/', views.movie_delete, name='movie_delete'),
]
