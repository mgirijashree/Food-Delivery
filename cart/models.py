from django.db import models
from django.conf import settings

from menu.models import FoodItem



class Cart(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cart"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.user.username





class CartItem(models.Model):

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items"
    )


    food = models.ForeignKey(
        FoodItem,
        on_delete=models.CASCADE
    )


    quantity = models.PositiveIntegerField(
        default=1
    )


    added_at = models.DateTimeField(
        auto_now_add=True
    )



    def subtotal(self):

        return self.food.price * self.quantity



    def __str__(self):

        return f"{self.food.name} ({self.quantity})"