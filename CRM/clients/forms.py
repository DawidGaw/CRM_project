from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    tags_input = forms.CharField(
        required=False,
        label="Tags",
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-user",
                "placeholder": "Add tags, separate by commas",
            }
        ),
    )

    class Meta:
        model = Client
        fields = [
            "company_name",
            "email",
            "phone_number",
            "address",
            "tax_number",
            "status",
        ]
