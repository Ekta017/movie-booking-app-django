from django.urls import path
from .views import seat_layout

urlpatterns = [
    path('seats/<int:movie_id>/', seat_layout, name='seat_layout'),
]