from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):

    class Meta:
        model = User

        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "role",
            "password1",
            "password2",
        )

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "w-full border rounded-lg p-3"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "w-full border rounded-lg p-3"
            }),
            "username": forms.TextInput(attrs={
                "class": "w-full border rounded-lg p-3"
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full border rounded-lg p-3"
            }),
            "role": forms.Select(attrs={
                "class": "w-full border rounded-lg p-3"
            }),
        }


class LoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "w-full border rounded-lg p-3"
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "w-full border rounded-lg p-3"
        })
    )