from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
import razorpay
import logging
import json

from .models import Payment

# Razorpay client setup
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

# Logger setup
logger = logging.getLogger(__name__)


def home(request):
    return render(request, 'payment.html', {
        'razorpay_key_id': settings.RAZORPAY_KEY_ID
    })


@csrf_exempt
def create_order(request):
    if request.method == "POST":
        try:
            # Parse amount from JSON body
            data = json.loads(request.body)
            amount_rupees = int(data.get("amount", 0))

            if amount_rupees <= 0:
                return JsonResponse({"error": "Invalid amount entered"}, status=400)

            amount_paise = amount_rupees * 100
            currency = "INR"

            order_data = {
                "amount": amount_paise,
                "currency": currency,
                "payment_capture": "1",
            }

            order = client.order.create(data=order_data)
            logger.info("Razorpay order created: %s", order)

            # Save initial Payment record to DB
            Payment.objects.create(
                razorpay_order_id=order['id'],
                amount=amount_paise,
                status='created'
            )

            return JsonResponse({
                "order_id": order["id"],
                "razorpay_key": settings.RAZORPAY_KEY_ID,
                "amount": amount_paise,
                "currency": currency
            })

        except Exception as e:
            logger.error("Error creating Razorpay order: %s", str(e))
            return JsonResponse({"error": "Something went wrong"}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)


@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        try:
            data = request.POST

            params_dict = {
                "razorpay_order_id": data.get("razorpay_order_id"),
                "razorpay_payment_id": data.get("razorpay_payment_id"),
                "razorpay_signature": data.get("razorpay_signature"),
            }

            logger.debug("Verifying payment: %s", params_dict)

            # Signature verification
            client.utility.verify_payment_signature(params_dict)

            # Update Payment object
            payment = Payment.objects.get(razorpay_order_id=params_dict["razorpay_order_id"])
            payment.razorpay_payment_id = params_dict["razorpay_payment_id"]
            payment.razorpay_signature = params_dict["razorpay_signature"]
            payment.status = "paid"
            payment.save()

            return JsonResponse({"status": "Payment verified successfully"})

        except Exception as e:
            logger.error("Payment verification failed: %s", str(e))
            return JsonResponse({
                "status": "Verification failed",
                "details": str(e)
            }, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
