"""pjt08 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views

app_name = "movies"

urlpatterns = [
    path('genres/', views.genre_list, name="genre_list"),
    path('genres/<int:id>/', views.genre_detail, name="genre_detail"),
    path('movies/', views.movie_list, name="movie_list"),
    path('movies/<int:id>/', views.movie_detail, name="movie_detail"),
    path('movies/<int:id>/reviews/', views.review_create, name="review_create"),
    path('reviews/<int:id>/', views.review_detail, name="review_detail"),
]
