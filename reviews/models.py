from django.db import models
from django.contrib.auth import get_user_model
from menu.models import FoodItem

User = get_user_model()


class Review(models.Model):

    RATING_CHOICES = [
        (1, "1 Star"),
        (2, "2 Stars"),
        (3, "3 Stars"),
        (4, "4 Stars"),
        (5, "5 Stars"),
    ]

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    food = models.ForeignKey(
        FoodItem,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
    )

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ("customer", "food")

    def __str__(self):
        return f"{self.food.name} - {self.customer.username} ({self.rating}★)"