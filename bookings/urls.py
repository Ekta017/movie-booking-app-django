from django.urls import path
from .views import create_booking, dummy_payment, payment_success

urlpatterns = [
    path('create/<int:seat_id>/', create_booking, name='create_booking'),
    path('payment/<int:booking_id>/', dummy_payment, name='dummy_payment'),
    path('success/<int:booking_id>/', payment_success, name='payment_success'),
]