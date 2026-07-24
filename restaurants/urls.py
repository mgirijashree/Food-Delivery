from django.urls import path
from . import views

urlpatterns = [

    path("", views.restaurant_list, name="restaurant_list"),

    path("add/", views.restaurant_create, name="restaurant_add"),

    path(
        "<int:pk>/menu/",
        views.restaurant_menu,
        name="restaurant_menu"
    ),

    
    path(
        "edit/<int:pk>/",
        views.restaurant_update,
        name="restaurant_edit",
    ),

    path(
        "delete/<int:pk>/",
        views.restaurant_delete,
        name="restaurant_delete",
    ),
]