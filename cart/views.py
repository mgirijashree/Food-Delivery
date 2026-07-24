from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from menu.models import FoodItem
from .models import Cart


@login_required
def cart_list(request):
    items = Cart.objects.filter(customer=request.user)

    total = sum(item.total_price for item in items)

    return render(
        request,
        "cart/cart.html",
        {
            "items": items,
            "total": total,
        },
    )


@login_required

def add_to_cart(request, id):

    food = get_object_or_404(
        FoodItem,
        id=id
    )


    cart = request.session.get(
        "cart",
        {}
    )


    food_id = str(food.id)


    if food_id in cart:

        cart[food_id] += 1

    else:

        cart[food_id] = 1


    request.session["cart"] = cart

    request.session.modified = True


    return redirect(
        request.META.get(
            "HTTP_REFERER",
            "/menu/"
        )
    )


@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(
        Cart,
        id=cart_id,
        customer=request.user,
    )

    cart_item.delete()

    return redirect("cart")