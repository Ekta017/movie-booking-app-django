from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from theatres.models import Seat


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    def is_expired(self):
        return timezone.now() > self.reserved_at + timedelta(minutes=5)

    def __str__(self):
        return f"{self.seat.seat_number} - {self.user.username}"