from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
import uuid

from orders.models import Order
from delivery.models import Delivery

from .models import Payment


@login_required
def payment(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        customer=request.user
    )

    errors = {}


    if request.method == "POST":

        payment_method = request.POST.get(
            "payment_method"
        )


        # -------------------------
        # Payment Method Validation
        # -------------------------

        if not payment_method:

            errors["payment_method"] = (
                "Please select a payment method."
            )


        # -------------------------
        # UPI Validation
        # -------------------------

        if payment_method == "UPI":

            upi_id = request.POST.get(
                "upi_id"
            )


            if not upi_id:

                errors["upi_id"] = (
                    "UPI ID is required."
                )


            elif "@" not in upi_id:

                errors["upi_id"] = (
                    "Enter a valid UPI ID."
                )



        # -------------------------
        # Card Validation
        # -------------------------

        if payment_method == "Card":

            card_number = request.POST.get(
                "card_number"
            )

            expiry = request.POST.get(
                "expiry"
            )

            cvv = request.POST.get(
                "cvv"
            )


            if not card_number:

                errors["card_number"] = (
                    "Card number is required."
                )


            elif not card_number.isdigit():

                errors["card_number"] = (
                    "Card number must contain only digits."
                )


            elif len(card_number) != 16:

                errors["card_number"] = (
                    "Card number must be 16 digits."
                )



            if not expiry:

                errors["expiry"] = (
                    "Expiry date is required."
                )



            if not cvv:

                errors["cvv"] = (
                    "CVV is required."
                )


            elif not cvv.isdigit():

                errors["cvv"] = (
                    "CVV must contain only digits."
                )


            elif len(cvv) != 3:

                errors["cvv"] = (
                    "CVV must be 3 digits."
                )



        # If validation fails

        if errors:

            return render(
                request,
                "payments/payment.html",
                {
                    "order": order,
                    "errors": errors,
                }
            )



        # -------------------------
        # Prevent Duplicate Payment
        # -------------------------

        payment_exists = Payment.objects.filter(
            order=order
        ).exists()


        if payment_exists:

            return redirect(
                "delivery_status",
                order.id
            )



        # -------------------------
        # Create Payment
        # -------------------------

        Payment.objects.create(

            order=order,

            payment_method=payment_method,

            payment_status="Paid",

            transaction_id=
            str(uuid.uuid4())[:12].upper(),

            paid_at=timezone.now()

        )



        # -------------------------
        # Create Delivery
        # -------------------------

        Delivery.objects.get_or_create(

            order=order,

            defaults={

                "delivery_address":
                "123, Anna Nagar, Chennai",

                "delivery_status":
                "Preparing",

                "estimated_time":
                "30-40 Minutes"

            }

        )



        return redirect(
            "delivery_status",
            order.id
        )



    return render(
        request,
        "payments/payment.html",
        {
            "order": order,
            "errors": errors
        }
    )




@login_required
def payment_success(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        customer=request.user
    )


    payment = Payment.objects.filter(
        order=order
    ).first()


    return render(
        request,
        "payments/payment_success.html",
        {
            "order": order,
            "payment": payment
        }
    )