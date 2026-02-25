from django.utils import timezone
from datetime import timedelta
from .models import Booking


class ReleaseExpiredSeatsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        expired_bookings = Booking.objects.filter(
            is_confirmed=False,
            reserved_at__lt=timezone.now() - timedelta(minutes=5)
        )

        for booking in expired_bookings:
            booking.seat.is_booked = False
            booking.seat.save()
            booking.delete()

        response = self.get_response(request)
        return response