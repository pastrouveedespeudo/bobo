from django import forms
from .models import image


class imagepost(forms.ModelForm):
    class Meta:
        model = image
        fields = [
            "image",

            ]

