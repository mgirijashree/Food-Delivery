from django.contrib import admin
from .models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "phone",
        "is_open",
    )

    search_fields = (
        "name",
        "owner__username",
    )

    list_filter = (
        "is_open",
    )