from django import forms
from .models import Restaurant


class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = "__all__"

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        common_class = (
            "w-full rounded-xl border-2 border-lime-300 "
            "bg-white px-4 py-3 text-gray-700 "
            "placeholder-gray-400 "
            "transition duration-200 "
            "hover:border-lime-500 "
            "focus:outline-none "
            "focus:border-lime-700 "
            "focus:ring-4 "
            "focus:ring-lime-200"
        )

        for name, field in self.fields.items():

            field.widget.attrs["class"] = common_class

        if "description" in self.fields:
            self.fields["description"].widget.attrs.update({
                "rows": 5
            })

        if "image" in self.fields:
            self.fields["image"].widget.attrs.update({
                "class":
                "w-full rounded-xl border-2 border-dashed border-lime-300 "
                "bg-lime-50 p-4 cursor-pointer "
                "hover:border-lime-600"
            })