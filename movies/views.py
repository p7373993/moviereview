from django.shortcuts import render, get_object_or_404
from .models import Movie
from .models import MovieCast


def index(request):
    movie_list = Movie.objects.order_by('-create_date')
    return render(request, 'movies/movie_list.html', {'movie_list': movie_list})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    cast_list = MovieCast.objects.filter(movie=movie)
    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'cast_list': cast_list,
    })
