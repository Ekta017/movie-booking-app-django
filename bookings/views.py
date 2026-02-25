from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

from .models import Booking
from theatres.models import Seat


@login_required
def create_booking(request, seat_id):
    seat = get_object_or_404(Seat, id=seat_id)

    if seat.is_booked:
        return render(request, 'bookings/seat_taken.html')

    booking = Booking.objects.create(
        user=request.user,
        seat=seat
    )

    return redirect('dummy_payment', booking_id=booking.id)


@login_required
def dummy_payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'payments/dummy_payment.html', {
        'booking': booking
    })


@login_required
def payment_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # Confirm booking
    booking.is_confirmed = True
    booking.seat.is_booked = True
    booking.seat.save()
    booking.save()

    # ================= SEND REAL EMAIL =================
    subject = "🎟️ Movie Ticket Booking Confirmation"
    message = f"""
Hello {booking.user.username},

Your movie ticket has been successfully booked 🎉

🎬 Theatre: {booking.seat.screen.theatre.name}
💺 Seat Number: {booking.seat.seat_number}

Please arrive at least 15 minutes before showtime.

Enjoy your movie 🍿
— BookMyShow Team
"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [booking.user.email],
        fail_silently=False
    )

    return render(request, 'payments/success.html', {
        'booking': booking
    })