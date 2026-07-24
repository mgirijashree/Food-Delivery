from django.db import models
from orders.models import Order


class Payment(models.Model):

    PAYMENT_METHODS = [
        ("COD", "Cash on Delivery"),
        ("UPI", "UPI"),
        ("Card", "Card"),
    ]

    PAYMENT_STATUS = [
        ("Pending", "Pending"),
        ("Paid", "Paid"),
        ("Failed", "Failed"),
    ]

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="payment",
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS,
        default="COD",
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="Pending",
    )

    transaction_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    paid_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Payment #{self.id}"