from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant
from .forms import RestaurantForm


def restaurant_list(request):

    restaurants = Restaurant.objects.all()

    return render(
        request,
        "restaurants/restaurant_list.html",
        {"restaurants": restaurants},
    )


def restaurant_create(request):

    if request.method == "POST":

        form = RestaurantForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            return redirect("restaurant_list")

    else:

        form = RestaurantForm()

    return render(
        request,
        "restaurants/restaurant_form.html",
        {"form": form},
    )


def restaurant_update(request, pk):

    restaurant = get_object_or_404(Restaurant, pk=pk)

    if request.method == "POST":

        form = RestaurantForm(
            request.POST,
            request.FILES,
            instance=restaurant,
        )

        if form.is_valid():

            form.save()

            return redirect("restaurant_list")

    else:

        form = RestaurantForm(instance=restaurant)

    return render(
        request,
        "restaurants/restaurant_form.html",
        {
            "form": form,
        },
    )


def restaurant_delete(request, pk):

    restaurant = get_object_or_404(Restaurant, pk=pk)

    if request.method == "POST":

        restaurant.delete()

        return redirect("restaurant_list")

    return render(
        request,
        "restaurants/restaurant_delete.html",
        {
            "restaurant": restaurant,
        },
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
            "foods": foods,
        }
    )