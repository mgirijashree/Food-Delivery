from django.contrib import admin
from .models import FoodItem


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "restaurant",
        "price",
    ]


    list_filter = [
        "restaurant",
    ]


    search_fields = [
        "name",
        "restaurant__name",
    ]