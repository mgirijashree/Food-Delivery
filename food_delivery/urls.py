from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.home, name="home"),

    path("accounts/", include("accounts.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("restaurants/", include("restaurants.urls")),
    path("menu/", include("menu.urls")),
    path("cart/", include("cart.urls")),
    path("orders/", include("orders.urls")),

    path("payments/", include("payments.urls")),
    path("delivery/", include("delivery.urls")),
    path("reviews/", include("reviews.urls")),
]