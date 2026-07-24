from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterForm, LoginForm


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Account created successfully.")

            return redirect("login")

    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def user_login(request):

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]

            password = form.cleaned_data["password"]

            user = authenticate(
                username=username,
                password=password
            )

            if user:

                login(request, user)

                return redirect("dashboard")

            messages.error(request, "Invalid username or password.")

    else:

        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})


def user_logout(request):

    logout(request)

    return redirect("login")