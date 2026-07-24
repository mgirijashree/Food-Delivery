from django.shortcuts import render, get_object_or_404

from .models import Restaurant



def restaurant_list(request):

    restaurants = Restaurant.objects.filter(
        is_open=True
    )

    return render(
        request,
        "restaurants/restaurant_list.html",
        {
            "restaurants": restaurants
        }
    )



def restaurant_menu(request, pk):

    restaurant = get_object_or_404(
        Restaurant,
        id=pk
    )


    foods = restaurant.food_items.all()


    return render(
        request,
        "restaurants/restaurant_menu.html",
        {
            "restaurant": restaurant,
            "foods": foods
        }
    )