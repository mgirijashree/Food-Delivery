from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from cart.models import Cart
from .models import Order, OrderItem


@login_required
def checkout(request):

    cart_items = Cart.objects.filter(customer=request.user)

    total = sum(item.total_price for item in cart_items)

    if request.method == "POST":

        if not cart_items.exists():
            return redirect("cart")

        order = Order.objects.create(
            customer=request.user,
            total_amount=total
        )

        for item in cart_items:

            OrderItem.objects.create(
                order=order,
                food=item.food,
                quantity=item.quantity,
                price=item.food.price,
            )

        cart_items.delete()

        return redirect("payment", order.id)

    return render(
        request,
        "orders/checkout.html",
        {
            "cart_items": cart_items,
            "total": total,
        },
    )


@login_required
def order_success(request, order_id):

    order = Order.objects.get(
        id=order_id,
        customer=request.user
    )

    return render(
        request,
        "orders/order_success.html",
        {
            "order": order,
        },
    )