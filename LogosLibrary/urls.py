"""LogosLibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from library import views as library
from users import views as users

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
   # path('users/', include(('users.urls', 'users'), namespace='users')),
    path('users/', include('django.contrib.auth.urls')),
    path('book_list/', library.book_list, name='book_list'),
    path('book/<int:pk>/view/', library.book_view, name='book_view'),
    path('magazine_list/', library.magazine_list, name='magazine_list'),
    path('magazine/<int:pk>/view/', library.magazine_view, name='magazine_view'),
    path('movie_list/', library.movie_list, name='movie_list'),
    path('movie/<int:pk>/view/', library.movie_view, name='movie_view'),
    path('', include('library.urls')),
    path('', include('users.urls')),
]
