from django import forms

from .models import Deal


class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = "__all__"

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "client": forms.Select(attrs={"class": "form-control"}),
            "value": forms.NumberInput(attrs={"class": "form-control"}),
            "stage": forms.Select(attrs={"class": "form-control"}),
            "probability": forms.NumberInput(attrs={"class": "form-control"}),
            "expected_close_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "owner": forms.Select(attrs={"class": "form-control"}),
        }
