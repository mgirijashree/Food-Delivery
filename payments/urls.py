from django.urls import path

from . import views


urlpatterns = [

    path(
        "<int:order_id>/",
        views.payment,
        name="payment"
    ),


    path(
        "<int:order_id>/success/",
        views.payment_success,
        name="payment_success"
    ),

]