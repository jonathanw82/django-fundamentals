from django.shortcuts import render


def intro(request):
    return render(request, 'movies/foo.html')


def first_movie(request):
    data = {'title': 'The Good, The Bad The Ugly',
            'synopsys': 'A western movie',
            'release': '1966'}
    return render(request, 'movies/first_movie.html', data)


def get_all_movies(request):
    data = {'movies': [{'title': '1- The Good, The Bad The Ugly',
                        'synopsys': 'A western movie',
                        'release': '1966'},

                       {'title': '2- The Good, The Bad The Ugly',
                        'synopsys': 'A western movie',
                        'release': '1966'},


                       {'title': '3- The Good, The Bad The Ugly',
                        'synopsys': 'A western movie',
                        'release': '1966'}, ]
            }
    return render(request, 'movies/all-movies.html', data)


    def get_all_movies(request):

        movies = Movies.objects.all()

        data = {'movies': movies}

        return render(request, 'movies/all-movies.html', data)
