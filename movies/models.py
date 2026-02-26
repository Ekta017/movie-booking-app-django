# from django.db import models
#
# class Movie(models.Model):
#     GENRE_CHOICES = [
#         ('Action', 'Action'),
#         ('Comedy', 'Comedy'),
#         ('Drama', 'Drama'),
#     ]
#
#     LANGUAGE_CHOICES = [
#         ('English', 'English'),
#         ('Hindi', 'Hindi'),
#     ]
#
#     title = models.CharField(max_length=200)
#     genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
#     language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
#     description = models.TextField()
#     trailer_url = models.URLField()
#     poster = models.ImageField(upload_to='posters/')
#     release_date = models.DateField()
#
#     def __str__(self):
#         return self.title

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=50)

    # ✅ Use external URLs instead of local images
    poster_url = models.URLField()
    trailer_url = models.URLField()

    def __str__(self):
        return self.title