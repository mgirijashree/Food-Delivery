from django.shortcuts import render
from django.db.models import Avg
from .models import FoodItem


def food_list(request):

    foods = FoodItem.objects.select_related(
        "restaurant"
    ).prefetch_related(
        "reviews"
    ).annotate(
        average_rating=Avg("reviews__rating")
    )

    return render(
        request,
        "menu/food_list.html",
        {
            "foods": foods
        }
    )