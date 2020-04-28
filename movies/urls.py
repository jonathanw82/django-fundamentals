from django.urls import path
from .views import intro, first_movie, get_all_movies, create, read, edit

urlpatterns = [
    path('intro/', intro),
    path('first_movie', first_movie),
    path('all-movies', get_all_movies),
    path('create', create),
    path('read', read),
    path('bannana', edit),
]
