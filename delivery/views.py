from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Delivery
from orders.models import Order


@login_required
def delivery_status(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        customer=request.user,
    )

    delivery = get_object_or_404(
        Delivery,
        order=order,
    )

    order_items = order.items.select_related("food")

    return render(
        request,
        "delivery/delivery_status.html",
        {
            "order": order,
            "delivery": delivery,
            "order_items": order_items,
        },
    )