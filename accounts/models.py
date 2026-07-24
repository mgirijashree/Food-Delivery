from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ("customer", "Customer"),
        ("restaurant", "Restaurant"),
        ("delivery", "Delivery Partner"),
        ("admin", "Admin"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="customer",
    )

    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.username