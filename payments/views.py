import razorpay
from django.conf import settings
from django.shortcuts import render

client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
)

def payment(request):
    order = client.order.create({
        "amount": 30000,
        "currency": "INR",
        "payment_capture": 1
    })
    return render(request, 'payments/pay.html', {'order': order})