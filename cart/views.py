from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from menu.models import FoodItem
from .models import Cart,CartItem




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
def add_to_cart(request, food_id):

    food = get_object_or_404(
        FoodItem,
        id=food_id
    )


    cart, created = Cart.objects.get_or_create(
        user=request.user
    )


    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        food=food
    )


    if not created:

        cart_item.quantity += 1


    cart_item.save()


    return redirect(
        request.META.get(
            "HTTP_REFERER",
            "food_list"
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