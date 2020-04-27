from django.shortcuts import render
from .models import Movie


def intro(request):
    return render(request, 'movies/foo.html')


def first_movie(request):
    data = {'title': 'The Good, The Bad The Ugly',
            'synopsys': 'A western movie',
            'release': '1966'}
    return render(request, 'movies/first_movie.html', data)


def get_all_movies(request):
    data = {'movies': [{'title': 'The Good, The Bad The Ugly',
                        'synopsys': 'A western movie',
                        'release_year': '1966',
                        'duration': '120'},

                       {'title': 'Star Wars',
                        'synopsys': 'Family Fude in space',
                        'release_year': '1975',
                        'duration': '185'},


                       {'title': 'Star Trek',
                        'synopsys': 'Blue Blooded alians in space',
                        'release_year': '1965',
                        'duration': '120'}, ]
            }
    return render(request, 'movies/all-movies.html', data)

    def create(request):

        movies = Movie(title='my Movie', synopsys='Something There',
                       release_year='1989', duration=180)
        movies.save()

        data = {'movies': movies}
        return render(request, 'movies/create.html', data)

    def read(request):

        movies = Movie.objects.all()
        data = {'movies': movies}

        return render(request, 'movies/read.html', data)
