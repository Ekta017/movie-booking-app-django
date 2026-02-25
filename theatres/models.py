from django.db import models

class Theatre(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Screen(models.Model):
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

class Seat(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.seat_number