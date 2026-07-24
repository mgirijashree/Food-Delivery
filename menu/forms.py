from django import forms
from .models import FoodCategory, FoodItem


class FoodCategoryForm(forms.ModelForm):
    class Meta:
        model = FoodCategory
        fields = "__all__"


class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = "__all__"