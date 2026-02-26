from django.shortcuts import render
from .models import Movie

def movie_list(request):
    genre = request.GET.get('genre')
    language = request.GET.get('language')

    movies = Movie.objects.all()

    if genre:
        movies = movies.filter(genre=genre)
    if language:
        movies = movies.filter(language=language)

    genres = Movie.objects.values_list('genre', flat=True).distinct()
    languages = Movie.objects.values_list('language', flat=True).distinct()

    return render(request, 'movies/movie_list.html', {
        'movies': movies,
        'genres': genres,
        'languages': languages
    })