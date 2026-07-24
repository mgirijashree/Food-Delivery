from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart_list, name="cart"),
    path("add/<int:food_id>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:cart_id>/", views.remove_from_cart, name="remove_from_cart"),
]