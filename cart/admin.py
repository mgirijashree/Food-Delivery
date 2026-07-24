from django.contrib import admin
from .models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "food",
        "quantity",
    )

    list_filter = (
        "customer",
    )