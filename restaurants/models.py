from django.db import models
from django.conf import settings


class Restaurant(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="restaurants",
        limit_choices_to={"role": "restaurant"},
    )

    name = models.CharField(max_length=150)
    description = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    image = models.ImageField(
        upload_to="restaurants/",
        blank=True,
        null=True
    )

    is_open = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name