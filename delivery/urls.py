from django.urls import path
from . import views

urlpatterns = [
    path(
        "<int:order_id>/",
        views.delivery_status,
        name="delivery_status",
    ),
]