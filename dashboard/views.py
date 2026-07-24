from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):

    role = request.user.role

    if role == "admin":
        return render(request, "dashboard/admin_dashboard.html")

    elif role == "restaurant":
        return render(request, "dashboard/restaurant_dashboard.html")

    elif role == "delivery":
        return render(request, "dashboard/delivery_dashboard.html")

    return render(request, "dashboard/customer_dashboard.html")