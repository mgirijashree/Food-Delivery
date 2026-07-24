from django.db import models
from orders.models import Order


class Delivery(models.Model):

    STATUS_CHOICES = [
        ("Preparing", "Preparing"),
        ("Out for Delivery", "Out for Delivery"),
        ("Delivered", "Delivered"),
    ]

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="delivery",
    )

    delivery_address = models.TextField()

    delivery_status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="Preparing",
    )

    estimated_time = models.CharField(
        max_length=100,
        default="30-40 Minutes",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Delivery #{self.order.id}"