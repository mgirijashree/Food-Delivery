from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from menu.models import FoodItem
from .models import Review


@login_required
def add_review(request, food_id):

    food = get_object_or_404(FoodItem, id=food_id)

    review = Review.objects.filter(
        customer=request.user,
        food=food
    ).first()

    errors = {}

    if request.method == "POST":

        rating = request.POST.get("rating")
        comment = request.POST.get("comment", "").strip()

        # Rating Required
        if not rating:
            errors["rating"] = "Please select a rating."

        if not errors:

            if review:

                review.rating = rating
                review.comment = comment
                review.save()

            else:

                Review.objects.update_or_create(
                customer=request.user,
                food=food,
                defaults={
                    "rating": rating,
                    "comment": comment,
                },
            )

            return redirect("delivery_status", order_id=food.order_set.last().id)

    return render(
        request,
        "reviews/add_review.html",
        {
            "food": food,
            "review": review,
            "errors": errors,
        },
    )