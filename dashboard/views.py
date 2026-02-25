from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from bookings.models import Booking
from theatres.models import Seat


@staff_member_required
def admin_dashboard(request):
    total_bookings = Booking.objects.count()
    confirmed_bookings = Booking.objects.filter(is_confirmed=True).count()
    pending_bookings = Booking.objects.filter(is_confirmed=False).count()

    total_revenue = confirmed_bookings * 300  # ₹300 per ticket

    most_booked_seats = (
        Seat.objects.filter(is_booked=True)
        .values('seat_number')
        .distinct()
    )

    context = {
        'total_bookings': total_bookings,
        'confirmed_bookings': confirmed_bookings,
        'pending_bookings': pending_bookings,
        'total_revenue': total_revenue,
        'most_booked_seats': most_booked_seats,
    }

    return render(request, 'dashboard/admin_dashboard.html', context)