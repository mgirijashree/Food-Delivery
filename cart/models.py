from django.conf import settings
from django.db import models
from menu.models import FoodItem


class Cart(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cart_items",
    )

    food = models.ForeignKey(
        FoodItem,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.quantity * self.food.price

    def __str__(self):
        return f"{self.customer.username} - {self.food.name}"