from django import forms

from .models import Client, Contact


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


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["contact_type", "contact_date", "note", "next_followup"]

        widgets = {
            "contact_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "next_followup": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"}
            ),
            "note": forms.Textarea(attrs={"class": "form-control"}),
            "contact_type": forms.Select(attrs={"class": "form-control"}),
        }
