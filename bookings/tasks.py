from django.utils import timezone
from datetime import timedelta
from .models import Booking


def release_expired_bookings():
    expired_bookings = Booking.objects.filter(
        is_confirmed=False,
        reserved_at__lt=timezone.now() - timedelta(minutes=5)
    )

    for booking in expired_bookings:
        booking.seat.is_booked = False
        booking.seat.save()
        booking.delete()