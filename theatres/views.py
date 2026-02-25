from django.shortcuts import render, get_object_or_404
from movies.models import Movie
from .models import Seat

def seat_layout(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all().order_by('seat_number')

    return render(request, 'theatres/seat_layout.html', {
        'movie': movie,
        'seats': seats
    })